menu = '''
1) topla
2)çıkar
3)çarp
4)böl
5) karesini hesapla
6)karekök al 
q) çıkış
'''
print(menu)
kontrol=True
while kontrol:
    seçim = input(' istediğniziz seçimi seçin:')
    if seçim == 'q':
        print('çıkış yapılıyor')
        kontrol = False
    elif seçim =='1':
        print('toplama işlemi')
        print('-' * 30 )
        topla1 = int(input('birinci sayıyı giriniz:'))
        topla2 = int(input('ikinci sayıyı giriniz:'))
        print(f'{topla1} + {topla2} = {topla1+topla2}')
    elif seçim =='2':
        print('çıkarma işlemi')
        print('-' * 30 )
        çıkar1 = int(input('birinci sayıyı giriniz:'))
        çıkar2 = int(input('ikinci sayıyı giriniz:'))
        print(f'{çıkar1} - {çıkar2} = {çıkar1-çıkar2}')
    elif seçim =='3':
        print('çarpma işlemi')
        print('-' * 30 )
        çarp1 = int(input('birinci sayıyı giriniz:'))
        çarp2 = int(input('ikinci sayıyı giriniz:'))
        print(f'{çarp1} * {çarp2} = {çarp1*çarp2}')
    elif seçim =='4':
        print('bölme işlemi')
        print('-' * 30 )
        böl1 = int(input('birinci sayıyı giriniz:'))
        böl2 = int(input('ikinci sayıyı giriniz:'))
        print(f'{böl1} / {böl2} = {böl1/böl2}')
    elif seçim =='5':
        print('kare alma işlemi')
        print('-' * 30 )
        kare = int(input('sayıyı giriniz:'))
        print(f'{kare} = {kare**2}')
        print(f'{böl1} / {böl2} = {böl1/böl2}')
    elif seçim =='6':
        print('karekök alma işlemi')
        print('-' * 30 )
        karekök = int(input('sayıyı giriniz:'))
        print(f'{karekök} ** {karekök ** 1/2}')
    else:
        print('yalış seçim')