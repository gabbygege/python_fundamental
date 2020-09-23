kamus = {}
kamus['anak'] = 'child'
kamus['ayah'] = 'father'
kamus['ibu'] = 'mother'

print(kamus)
print(kamus['ayah'])
print(kamus['ibu'])

print('data ini dikirimkan oleh server gojek, utk ksh info driver')
data_dari_server_gojek = {
    'tanggal': '2020-06-10',
    'driver_list': [{'gabby': 'D999AA'}, {'kent': 'B123BC'}, {'michael': 'A888ZZ'}]
}
print(data_dari_server_gojek)
print(f"driver sekitar sini: {data_dari_server_gojek['driver_list']}")
print(f"driver #1 {data_dari_server_gojek['driver_list'][0]}")
print(f"plat nomor michael'{data_dari_server_gojek['driver_list'][2]}")
