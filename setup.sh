mkdir -p download

wget -P download/ -N https://pharmgkb-owl.googlecode.com/files/mesh.owl.gz
gunzip -c download/mesh.owl.gz > download/mesh.owl

python utils/make_mesh_mapping.py -x download/mesh.owl -o meshid_map.txt
