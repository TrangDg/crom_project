import csv
import vocab_gci as v
from cromulent.model import factory, ManMadeObject, Material, Type, Place, \
	Identifier, Acquisition, TimeSpan, Actor, InformationObject, Production
from cromulent.vocab import AccessionNumber, Name, Color, instances, Department, \
	Description, Barcode, CatalogNumber

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
			s = ManMadeObject(label="Sample Object")

		# Sample Identification/General Information
			# AccessionNumber is used for now, will a new class Barcode - aat:300343361
			s.identified_by = Barcode(label="Full Barcode", value=rec['fbarcode']) 
			s.identified_by = Barcode(label="Old Barcode", value=rec['obarcode'])
			s.identified_by = Name(label="Common Name", value=rec['name'])
			s.identified_by = Name(label="Additional Names", value=rec['add_names'])
			
			# Sample Type
			if rec['samp_type']:
				s.classified_as = instances[rec['samp_type'].lower()]
			
			# Typical use
			if rec['typ_use']:
				s.as_general_use = instances[rec['typ_use'].lower()]
			
			# Physical Form
			if rec['phys_form']:
				pf = rec['phys_form'].split()
				if len(pf) < 4:
					i = 0
					while i <= 2:
						s.classified_as = instances[pf[i].lower().replace(',', '')]
						i += 1
						break
				else:
					s.referred_to_by = Description(label="Sample Type", value=rec['phys_form'])

			# Color
			if rec['color']:
				s.classified_as = instances[rec['color']]
			
			# Natural/Synthetic
			if rec['nat_syn']:
				s.classified_as = instances[rec['nat_syn'].lower()]
			elif rec[nat_syn] == "Unknown":
				s.classified_as = Type(label="Natural/Synthetic", value="Unknown") 

			# Grid Location: lab shelf/storage?
			loc = Place()
			if rec['grid_loc']:
				loc.identified_by = Identifier(label="Grid Location", value=rec['grid_loc'])
				s.current_location = loc 
			
			# Index (CI) No., Preparation, Certified Standard

		# Acquisition Information

			acq = Acquisition()
			gci = Department("http://www.getty.edu/conservation/", label="Getty Research Institute")
			s.changed_ownership_through = acq
			acq.transferred_title_to = gci
			# Acquisition Date
			if rec['acq_date']:
				acq.timespan = TimeSpan(label=rec['acq_date'])

			# Acquired by
			if rec['acq_by']:
				emp = Actor(label=rec['acq_by'])
				acq.carried_out_by = emp
				emp.member_of = gci

			# Acquired from, debating whether it should be Actor or Group,
			# so info of person in contact can be linked
			if rec['acq_from']:
				acq.transferred_title_from = Actor(label=rec['acq_from'])

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





