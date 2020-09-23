anak = []
anak.append('Gabby')
anak.append('Kent')
anak.append('Michael')
print(anak)

print('\nsapa anak ke-2')
print(f'hai {anak[1]}')

for a in anak:
    print(f'hai {a}')

print('\nsapa semua anak: cara ribet')
for a in range(0, len(anak)):
    print(f'{a+1} hai {anak[a]}')

