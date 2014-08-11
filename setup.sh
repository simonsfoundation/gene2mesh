mkdir -p download

wget -P download/ -N https://pharmgkb-owl.googlecode.com/files/mesh.owl.gz
gunzip -c download/mesh.owl.gz > download/mesh.owl

python utils/make_mesh_mapping.py -x download/mesh.owl -o meshid_map.txt

python utils/make_mesh_mapping.py -x download/mesh.owl -o meshid_anatomy_map.txt -c A
python utils/make_mesh_mapping.py -x download/mesh.owl -o meshid_disease_map.txt -c C

bash retrieve.sh meshid_anatomy_map.txt output-anatomy
bash retrieve.sh meshid_disease_map.txt output-disease
