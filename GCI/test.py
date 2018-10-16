import csv
import vocab_gci as v

from cromulent.model import factory, ManMadeObject, Material, Type, Place, \
	Identifier, Acquisition, TimeSpan, Actor, InformationObject, Production, \
	Person
from cromulent.vocab import PrimaryName, Name, Color, instances, Department, \
	Description, Barcode, CatalogNumber
from dateparser import parse
from datetime import timedelta

factory.validate_profile = False


def main():
	f = open("ref_col.csv", "r")
	r = csv.reader(f)

	next(r) #Skip header
	headers = ["acq_by", "acq_from", "acq_date", "add_names", "avai_data", "cat", 
		"certified", "chem_comp", "CAS", "chem_form", "chem_name", "col_name", "color",
		"CI", "name", "comp_type", "contact", "email", "experiments", "fire", "formulation",
		"fbarcode", "geo_org", "grid_loc", "health", "manufacturer", "mass_vol", "mix_pigment",
		"mix_type", "MSDS", "nat_syn", "notes", "obarcode", "org_date", "other_safe", 
		"part_col", "phone", "phys_form", "prep", "reactivity", "samp_type", "typ_use",
		"warning", "borrower", "inv_status"]
	for counter, row in enumerate(r):
		rec = dict(zip(headers, row))
		# Testing first two rows
		if counter < 2: 
			s = ManMadeObject(label=rec['name'])

		# Sample Identification/General Information
			
			s.identified_by = Barcode(label="Full Barcode", value=rec['fbarcode']) 
			s.identified_by = Barcode(label="Old Barcode", value=rec['obarcode'])
			s.identified_by = PrimaryName(label="Common Name", value=rec['name'])
			s.identified_by = Name(label="Additional Names", value=rec['add_names'])
			
			# Sample Type
			if rec['samp_type']:
				try:
					s.classified_as = instances[rec['samp_type'].lower()]
				except:
					s.referred_to_by = Description(label="Sample Type", value=rec['samp_type'])
			
			# Typical use
			if rec['typ_use']:
				use = rec['typ_use'].split('/')
				for i in range(len(use)):
					try:
						s.as_general_use = instances[use[i].lower().strip()]
					except:
						s.referred_to_by = Description(label="Typical Use", value=use[i])
			
			# Physical Form
			if rec['phys_form']:
				pf = rec['phys_form'].split()

				if len(pf) < 4:
					l = []
					
					for i in range(len(pf)):
						try:
							s.classified_as = instances[pf[i].lower().replace(',', '').strip()]
						except:
							l.append(pf[i])
					# return(l)
					l_join = " ".join(l)
							
					s.referred_to_by = Description(label="Physical Form", value=l_join)
							# continue
						
				else:
					s.referred_to_by = Description(label="Physical Form", value=rec['phys_form'])


			# Color
			if rec['color']:
				try:
					s.classified_as = instances[rec['color']]
				except:
					s.referred_to_by = Description(label="Color", value=rec['color'])
			
			# Natural/Synthetic
			if rec['nat_syn']:
				s.classified_as = instances[rec['nat_syn'].lower()]
			elif rec['nat_syn'] == "Unknown":
				s.classified_as = Type(label="Natural/Synthetic", value="Unknown") 

			# Grid Location: lab shelf/storage?
			loc = Place()
			if rec['grid_loc']:
				loc.identified_by = Identifier(label="Grid Location", value=rec['grid_loc'])
				s.current_location = loc 
			
			# Index (CI) No., Preparation, Certified Standard

		# Acquisition Information

			acq = Acquisition()
			
			s.changed_ownership_through = acq
			acq.transferred_title_to = v.dept['GCI']
			# Acquisition Date
			if rec['acq_date']:
				adate = rec['acq_date']
				tspan = TimeSpan(label=adate)
				if len(adate) == 4:
					tspan.begin_of_the_begin = str(parse(adate + 'January', settings={'PREFER_DAY_OF_MONTH': 'first'}))
					tspan.end_of_the_end = str(parse(str(int(adate)+1) + 'January', settings={'PREFER_DAY_OF_MONTH': 'first'}))
				elif 'ca.' in adate or 'Spring' in adate:
					y = adate.split()[1]
					tspan.begin_of_the_begin = str(parse(y + 'January', settings={'PREFER_DAY_OF_MONTH': 'first'}))	
					tspan.end_of_the_end = str(parse(str(int(y)+1) + 'January', settings={'PREFER_DAY_OF_MONTH': 'first'}))
				elif '-' in adate:
					y = adate.split('-')
					start_year = y[0].strip()
					end_year = y[1].strip()	
					if len(start_year) > 2:
						tspan.begin_of_the_begin = str(parse(start_year + 'January', settings={'PREFER_DAY_OF_MONTH': 'first'}))	
						tspan.end_of_the_end = str(parse(str(int(end_year)+1) + 'January', settings={'PREFER_DAY_OF_MONTH': 'first'}))
					else:
						tspan.begin_of_the_begin = str(parse(adate, settings={'PREFER_DAY_OF_MONTH': 'first'}))
						tspan.end_of_the_end = str(parse(adate + ' 23:59:59', settings={'PREFER_DAY_OF_MONTH': 'last'}))
				else:
					tspan.begin_of_the_begin = str(parse(adate, settings={'PREFER_DAY_OF_MONTH': 'first'}))
					tspan.end_of_the_end = str(parse(adate, settings={'PREFER_DAY_OF_MONTH': 'last'}) + timedelta(days=1)) 


				acq.timespan = tspan

			# Acquired by
			if rec['acq_by']:
				p = rec['acq_by'].split('-')
				pname = p[0]
				dpt = p[-1]
				if pname in v.person:
					emp = v.person[pname]
				else:
					emp = Person(label=pname)
				acq.carried_out_by = emp
				if dpt in v.dept:
					emp.member_of = v.dept[dpt]


			# Acquired from, debating whether it should be Actor or Group,
			# so info of person in contact can be linked
			if rec['acq_from']:
				if rec['acq_from'] in v.sellers:
					seller = v.sellers[rec['acq_from']]
				else:
					seller = Actor(label=rec['acq_from'])
				acq.transferred_title_from = seller

			# Geographic Origin
			if rec['geo_org']:
				prod = Production()
				origin = Place(label="Geographic Origin")
				origin.identified_by = Name(value=rec['geo_org'])
				prod.took_place_at = origin
				s.produced_by = prod

			# Catalog No.
			if rec['cat']:
				s.identified_by = CatalogNumber(label="Catalog No.", value=rec['cat'])

		# Miscellaneous
			# Notes
			if rec['notes']:
				io = InformationObject(value=rec['notes'])
				io.classified_as = instances["notes"]





			print(factory.toString(s, compact=False))

		# break 


main()





