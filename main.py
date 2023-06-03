import cx_Oracle
import random
import datetime
cx_Oracle.init_oracle_client(lib_dir=r"C:\oracle_cx")
rows = 0
sd = datetime.date(2021, 1, 1)


def Random_number():
    rand = random.randint(0, 200)
    rand = str(rand)
    return rand


def Random_street():
    with open("ulice.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split('\n')))
    rand = random.choice(words)
    return rand


def Random_city():
    with open("miejscowosci.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split('\n')))
    rand = random.choice(words)
    return rand


def Random_post_code():
    rand1 = random.randint(0, 99)
    rand1 = str(rand1)
    rand2 = random.randint(100, 999)
    rand2 = str(rand2)
    rand = rand1+'-'+rand2
    return rand


def Random_name():
    with open("imiona.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split('\n')))
    rand = random.choice(words)
    return rand


def Random_surname():
    with open("nazwiska.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split('\n')))
    rand = random.choice(words)
    return rand


def Random_work():
    with open("praca.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split('\n')))
    rand = random.choice(words)
    return rand


def Random_company():
    with open("firma.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split('\n')))
    rand = random.choice(words)
    return rand


def Random_country():
    with open("kraje.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split('\n')))
    rand = random.choice(words)
    return rand


def Random_date():
    start_date = datetime.date(1960, 1, 1)
    end_date = datetime.date(2001, 1, 1)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    random_date = str(random_date)
    return random_date


def Random_date2():
    start_date = datetime.date(2001, 1, 1)
    end_date = datetime.date(2021, 1, 1)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    random_date = str(random_date)
    return random_date


def Random_date3():
    start_date = datetime.date(2021, 1, 1)
    end_date = datetime.date(2021, 11, 4)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    random_date = str(random_date)
    return random_date


def Random_salary():
    rand = random.randint(2500, 5000)
    rand = str(rand)
    return rand


def Random_hour():
    rand = random.randint(0, 10)
    rand = str(rand)
    return rand


def Random_hour2():
    rand1 = random.randint(0, 24)
    rand1 = str(rand1)
    rand2 = random.randint(0, 60)
    rand2 = str(rand2)
    rand = rand1 + ':' + rand2
    return rand


def Random_fk(fk):
    rand = random.randint(1, fk)
    rand = str(rand)
    return rand


def Random_pesel():
    rand = random.randint(10000000000, 99999999999)
    rand = str(rand)
    return rand


def Random_telephone():
    rand = random.randint(100000000, 999999999)
    rand = str(rand)
    return rand


def Random_med():
    with open("leki.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split('\n')))
    rand = random.choice(words)
    return rand


def Random_med_cat():
    with open("leki.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split('\n')))
    rand = random.choice(words)
    return rand


def Random_price():
    rand = random.uniform(1.0, 200.0)
    rand = round(rand, 2)
    rand = str(rand)
    return rand


def Random_date4(rand):
    if rand == 1:
        global sd
        sd = sd + datetime.timedelta(days=1)
    random_date = str(sd)
    return random_date


def Date(rand, sd):
    if rand == 1:
        sd = sd + datetime.timedelta(days=1)
    return sd


def Random_discount():
    rand = random.uniform(0.00, 1.00)
    rand = round(rand, 2)
    rand = str(rand)
    return rand


def Insert_Adres_klienta(connection, rows):
    last_id_table = [0]
    cursor = connection.cursor()
    cursor.execute("""select id_Adres_klienta from Adres_Klienta""")
    connection.commit()
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        last_id_table = row
    last_id = last_id_table[0]
    last_id += 1
    text_file = open("insert.txt", "a")
    for i in range(rows):
        last_id = str(last_id)
        rand_street = Random_street()
        rand_number = Random_number()
        rand_city = Random_city()
        rand_post_code = Random_post_code()
        cursor = connection.cursor()
        cursor.execute("insert into Adres_klienta values("+last_id+",\'"+rand_street+"\',\'"+rand_number+"\',\'"+rand_city+"\',\'"+rand_post_code+"\')")
        n = 'insert into Adres_klienta values(' + last_id + ',\''+rand_street+'\',\''+rand_number+'\',\''+rand_city+'\',\''+rand_post_code+'\');\n'
        text_file.write(n)
        connection.commit()
        last_id = int(last_id)
        last_id += 1
    text_file.write('\n')
    text_file.close()
    print('insert Adres_klienta')


def Insert_Apteka(connection, rows):
    last_id_table = [0]
    cursor = connection.cursor()
    cursor.execute("""select id_Apteka from Apteka""")
    connection.commit()
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        last_id_table = row
    last_id = last_id_table[0]
    last_id += 1
    text_file = open("insert.txt", "a")
    for i in range(rows):
        last_id = str(last_id)
        rand_street = Random_street()
        rand_city = Random_city()
        rand_name = Random_name()
        rand_surname = Random_surname()
        cursor = connection.cursor()
        cursor.execute("insert into Apteka values("+last_id+",\'"+rand_street+"\',\'"+rand_city+"\',\'"+rand_name+"\',\'"+rand_surname+"\')")
        n = 'insert into Apteka values(' + last_id + ',\''+rand_street+'\',\''+rand_city+'\',\''+rand_name+'\',\''+rand_surname+'\');\n'
        text_file.write(n)
        connection.commit()
        last_id = int(last_id)
        last_id += 1
    text_file.write('\n')
    text_file.close()
    print('insert Apteka')


def Insert_Praca_w_laboratorium(connection, rows):
    last_id_table = [0]
    cursor = connection.cursor()
    cursor.execute("""select id_Praca_w_laboratorium from Praca_w_laboratorium""")
    connection.commit()
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        last_id_table = row
    last_id = last_id_table[0]
    last_id += 1
    text_file = open("insert.txt", "a")
    for i in range(rows):
        last_id = str(last_id)
        rand_work = Random_work()
        cursor = connection.cursor()
        cursor.execute("insert into Praca_w_laboratorium values("+last_id+",\'"+rand_work+"\')")
        n = 'insert into Praca_w_laboratorium values(' + last_id + ',\''+rand_work+'\');\n'
        text_file.write(n)
        connection.commit()
        last_id = int(last_id)
        last_id += 1
    text_file.write('\n')
    text_file.close()
    print('insert Praca_w_laboratorium')


def Insert_Hurtownia(connection, rows):
    last_id_table = [0]
    cursor = connection.cursor()
    cursor.execute("""select id_Hurtownia from Hurtownia""")
    connection.commit()
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        last_id_table = row
    last_id = last_id_table[0]
    last_id += 1
    text_file = open("insert.txt", "a")
    for i in range(rows):
        last_id = str(last_id)
        rand_company = Random_company()
        rand_city = Random_city()
        rand_name = Random_name()
        rand_surname = Random_surname()
        rand_post_code = Random_post_code()
        cursor = connection.cursor()
        cursor.execute("insert into Hurtownia values("+last_id+",\'"+rand_company+"\',\'"+rand_name+"\',\'"+rand_surname+"\',\'"+rand_city+"\',\'"+rand_post_code+"\')")
        n = 'insert into Hurtownia values(' + last_id + ',\''+rand_company+'\',\''+rand_name+'\',\''+rand_surname+'\',\''+rand_city+'\',\''+rand_post_code+'\');\n'
        text_file.write(n)
        connection.commit()
        last_id = int(last_id)
        last_id += 1
    text_file.write('\n')
    text_file.close()
    print('insert Hurtownia')


def Insert_Producenci(connection, rows):
    last_id_table = [0]
    cursor = connection.cursor()
    cursor.execute("""select id_Producenci from Producenci""")
    connection.commit()
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        last_id_table = row
    last_id = last_id_table[0]
    last_id += 1
    text_file = open("insert.txt", "a")
    for i in range(rows):
        last_id = str(last_id)
        rand_company = Random_company()
        rand_country = Random_country()
        cursor = connection.cursor()
        cursor.execute("insert into Producenci values("+last_id+",\'"+rand_company+"\',\'"+rand_country+"\')")
        n = 'insert into Producenci values(' + last_id + ',\''+rand_company+'\',\''+rand_country+'\');\n'
        text_file.write(n)
        connection.commit()
        last_id = int(last_id)
        last_id += 1
    text_file.write('\n')
    text_file.close()
    print('insert Producenci')


def Insert_Pracownicy(connection, rows):
    last_id_table = [0]
    cursor = connection.cursor()
    cursor.execute("""select id_Pracownicy from Pracownicy""")
    connection.commit()
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        last_id_table = row
    last_id = last_id_table[0]
    last_id += 1
    text_file = open("insert.txt", "a")
    for i in range(rows):
        last_id = str(last_id)
        rand_name = Random_name()
        rand_surname = Random_surname()
        rand_date = Random_date()
        rand_date2 = Random_date2()
        rand_salary = Random_salary()
        rand_compamy = Random_company()
        cursor = connection.cursor()
        cursor.execute("insert into Pracownicy values("+last_id+",\'"+rand_name+"\',\'"+rand_surname+"\', to_date(\'"+rand_date+"\',\'RRRR-MM-DD\'),\'"+rand_salary+"\',to_date(\'"+rand_date2+"\',\'RRRR-MM-DD\'),\'"+rand_compamy+"\')")
        n = 'insert into Pracownicy values(' + last_id + ',\''+rand_name+'\',\''+rand_surname+'\' ,to_date(\''+rand_date+'\',\'RRRR-MM-DD\'), \''+rand_salary+'\',to_date(\''+rand_date2+'\',\'RRRR-MM-DD\'));\n'
        text_file.write(n)
        connection.commit()
        last_id = int(last_id)
        last_id += 1
    text_file.write('\n')
    text_file.close()
    print('insert Pracownicy')


def Insert_Laboratorium(connection, rows):
    last_id_table = [0]
    cursor = connection.cursor()
    cursor.execute("""select id_Laboratorium from Laboratorium""")
    connection.commit()
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        last_id_table = row
    last_id = last_id_table[0]

    fk_id_table = [0]
    cursor = connection.cursor()
    cursor.execute("""select id_pracownicy from Pracownicy""")
    connection.commit()
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        fk_id_table = row
    fk_id = fk_id_table[0]

    fk2_id_table = [0]
    cursor = connection.cursor()
    cursor.execute("""select id_praca_w_laboratorium from Praca_w_laboratorium""")
    connection.commit()
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        fk2_id_table = row
    fk2_id = fk2_id_table[0]

    last_id += 1
    text_file = open("insert.txt", "a")
    for i in range(rows):
        last_id = str(last_id)
        rand_date3 = Random_date3()
        rand_hour = Random_hour()
        rand_hour2 = Random_hour2()
        rand_fk = Random_fk(fk_id)
        rand_fk2 = Random_fk(fk2_id)
        cursor = connection.cursor()
        cursor.execute("insert into Laboratorium values("+last_id+",to_date(\'"+rand_date3+"\',\'RRRR-MM-DD\'),\'"+rand_hour+"\',\'"+rand_hour2+"\',\'"+rand_fk+"\',\'"+rand_fk2+"\')")
        n = 'insert into Laboratorium values(' + last_id + ',to_date(\''+rand_date3+'\',\'RRRR-MM-DD\'),\''+rand_hour+'\',\''+rand_hour2+'\',\''+rand_fk+'\',\''+rand_fk2+'\');\n'
        text_file.write(n)
        connection.commit()
        last_id = int(last_id)
        last_id += 1
    text_file.write('\n')
    text_file.close()
    print('insert Laboratorium')


def Insert_Klienci(connection, rows):
    last_id_table = [0]
    cursor = connection.cursor()
    cursor.execute("""select id_Klienci from Klienci""")
    connection.commit()
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        last_id_table = row
    last_id = last_id_table[0]

    fk_id_table = [0]
    cursor = connection.cursor()
    cursor.execute("""select id_adres_klienta from Adres_klienta""")
    connection.commit()
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        fk_id_table = row
    fk_id = fk_id_table[0]

    last_id += 1
    text_file = open("insert.txt", "a")
    for i in range(rows):
        last_id = str(last_id)
        rand_name = Random_name()
        rand_surname = Random_surname()
        rand_pesel = Random_pesel()
        rand_telephone = Random_telephone()
        rand_fk = Random_fk(fk_id)
        cursor = connection.cursor()
        cursor.execute("insert into Klienci values(" + last_id + ",\'" + rand_name + "\',\'" + rand_surname + "\',\'" + rand_pesel + "\',\'" + rand_telephone + "\',\'" + rand_fk + "\')")
        n = 'insert into Klienci values(' + last_id + ',\'' + rand_name + '\',\'' + rand_surname + '\',\'' + rand_pesel + '\',\'' + rand_telephone + '\',\'' + rand_fk + '\');\n'
        text_file.write(n)
        connection.commit()
        last_id = int(last_id)
        last_id += 1
    text_file.write('\n')
    text_file.close()
    print('insert Klienci')


def Insert_Leki(connection, rows):
    last_id_table = [0]
    cursor = connection.cursor()
    cursor.execute("""select id_Leki from Leki""")
    connection.commit()
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        last_id_table = row
    last_id = last_id_table[0]

    fk_id_table = [0]
    cursor = connection.cursor()
    cursor.execute("""select id_hurtownia from Hurtownia""")
    connection.commit()
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        fk_id_table = row
    fk_id = fk_id_table[0]

    fk2_id_table = [0]
    cursor = connection.cursor()
    cursor.execute("""select id_producenci from Producenci""")
    connection.commit()
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        fk2_id_table = row
    fk2_id = fk2_id_table[0]

    last_id += 1
    text_file = open("insert.txt", "a")
    for i in range(rows):
        last_id = str(last_id)
        rand_med = Random_med()
        rand_med_cat = Random_med_cat()
        rand_price = Random_price()
        rand_fk = Random_fk(fk_id)
        rand_fk2 = Random_fk(fk2_id)
        cursor = connection.cursor()
        cursor.execute("insert into Leki values("+last_id+",\'"+rand_med+"\',\'"+rand_med_cat+"\',\'"+rand_price+"\',\'"+rand_fk+"\',\'"+rand_fk2+"\')")
        n = 'insert into Leki values(' + last_id + ',\''+rand_med+'\',\''+rand_med_cat+'\',\''+rand_price+'\',\''+rand_fk+'\',\''+rand_fk2+'\');\n'
        text_file.write(n)
        connection.commit()
        last_id = int(last_id)
        last_id += 1
    text_file.write('\n')
    text_file.close()
    print('insert Leki')


def Insert_Partia_leku(connection, rows):
    last_id_table = [0]
    cursor = connection.cursor()
    cursor.execute("""select id_Partia_leku from Partia_leku""")
    connection.commit()
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        last_id_table = row
    last_id = last_id_table[0]

    fk_id_table = [0]
    cursor = connection.cursor()
    cursor.execute("""select id_leki from Leki""")
    connection.commit()
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        fk_id_table = row
    fk_id = fk_id_table[0]

    fk2_id_table = [0]
    cursor = connection.cursor()
    cursor.execute("""select id_apteka from Apteka""")
    connection.commit()
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        fk2_id_table = row
    fk2_id = fk2_id_table[0]

    last_id += 1
    text_file = open("insert.txt", "a")
    for i in range(rows):
        last_id = str(last_id)
        rand_number = Random_number()
        rand_date3 = Random_date3()
        rand_number2 = Random_number()
        rand_price = Random_price()
        rand_fk = Random_fk(fk_id)
        rand_fk2 = Random_fk(fk2_id)
        cursor = connection.cursor()
        cursor.execute("insert into Partia_leku values("+last_id+",\'"+rand_number+"\',to_date(\'"+rand_date3+"\',\'RRRR-MM-DD\'),\'"+rand_number2+"\',\'"+rand_price+"\',\'"+rand_fk+"\',\'"+rand_fk2+"\')")
        n = 'insert into Partia_leku values(' + last_id + ',\''+rand_number+'\',to_date(\''+rand_date3+'\',\'RRRR-MM-DD\'),\''+rand_number2+'\',\''+rand_price+'\',\''+rand_fk+'\',\''+rand_fk2+'\');\n'
        text_file.write(n)
        connection.commit()
        last_id = int(last_id)
        last_id += 1
    text_file.write('\n')
    text_file.close()
    print('insert Partia_leku')


def Insert_Zamowienia(connection, rows):
    last_id_table = [0]
    cursor = connection.cursor()
    cursor.execute("""select id_Zamowienia from Zamowienia""")
    connection.commit()
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        last_id_table = row
    last_id = last_id_table[0]

    fk_id_table = [0]
    cursor = connection.cursor()
    cursor.execute("""select id_klienci from Klienci""")
    connection.commit()
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        fk_id_table = row
    fk_id = fk_id_table[0]

    fk2_id_table = [0]
    cursor = connection.cursor()
    cursor.execute("""select id_Pracownicy from Pracownicy""")
    connection.commit()
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        fk2_id_table = row
    fk2_id = fk2_id_table[0]

    fk3_id_table = [0]
    cursor = connection.cursor()
    cursor.execute("""select id_apteka from Apteka""")
    connection.commit()
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        fk3_id_table = row
    fk3_id = fk3_id_table[0]

    last_id += 1

    text_file = open("insert.txt", "a")
    for i in range(rows):
        last_id = str(last_id)
        rand_pesel = Random_pesel()
        rand = random.randint(0, 1)

        rand_date4 = Random_date4(rand)
        rand_fk = Random_fk(fk_id)
        rand_fk2 = Random_fk(fk2_id)
        rand_fk3 = Random_fk(fk3_id)
        cursor = connection.cursor()
        cursor.execute("insert into Zamowienia values("+last_id+",\'"+rand_pesel+"\',to_date(\'"+rand_date4+"\',\'RRRR-MM-DD\'),\'"+rand_fk+"\',\'"+rand_fk2+"\',\'"+rand_fk3+"\')")
        n = 'insert into Zamowienia values(' + last_id + ',\''+rand_pesel+'\',to_date(\''+rand_date4+'\',\'RRRR-MM-DD\'),\''+rand_fk+'\',\''+rand_fk2+'\',\''+rand_fk3+'\');\n'
        text_file.write(n)
        connection.commit()
        last_id = int(last_id)
        last_id += 1
    text_file.write('\n')
    text_file.close()
    print('insert Zamowienia')


def Insert_Informacje_o_zamowieniu(connection, rows):
    last_id_table = [0]
    cursor = connection.cursor()
    cursor.execute("""select id_Informacje_o_zamowieniu from Informacje_o_zamowieniu""")
    connection.commit()
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        last_id_table = row
    last_id = last_id_table[0]

    fk_id_table = [0]
    cursor = connection.cursor()
    cursor.execute("""select id_zamowienia from Zamowienia""")
    connection.commit()
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        fk_id_table = row
    fk_id = fk_id_table[0]

    fk2_id_table = [0]
    cursor = connection.cursor()
    cursor.execute("""select id_leki from Leki""")
    connection.commit()
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        fk2_id_table = row
    fk2_id = fk2_id_table[0]

    last_id += 1
    text_file = open("insert.txt", "a")
    for i in range(rows):
        last_id = str(last_id)
        rand_price = Random_price()
        rand_discount = Random_discount()
        rand_fk = Random_fk(fk_id)
        rand_fk2 = Random_fk(fk2_id)
        cursor = connection.cursor()
        cursor.execute("insert into Informacje_o_zamowieniu values("+last_id+",\'"+rand_price+"\',\'"+rand_discount+"\',\'"+rand_fk+"\',\'"+rand_fk2+"\')")
        n = 'insert into Informacje_o_zamowieniu values(' + last_id + ',\''+rand_price+'\',\''+rand_discount+'\',\''+rand_fk+'\',\''+rand_fk2+'\');\n'
        text_file.write(n)
        connection.commit()
        last_id = int(last_id)
        last_id += 1
    text_file.write('\n')
    text_file.close()
    print('insert Informacje_o_zamowieniu')


ip = '217.173.198.135'
port = 1522
SID = 'orcltp'
dsn_tns = cx_Oracle.makedsn(ip, port, SID)
connection = cx_Oracle.connect('s97628', 'lukluk12', dsn_tns)

print('Ile wierszy dodać?')
rows = int(input())

# Insert_Adres_klienta(connection, rows)
# Insert_Apteka(connection, rows)
# Insert_Praca_w_laboratorium(connection, rows)
# Insert_Hurtownia(connection, rows)
# Insert_Producenci(connection, rows)
# Insert_Pracownicy(connection, rows)
# Insert_Laboratorium(connection, rows)
# Insert_Klienci(connection, rows)
# Insert_Leki(connection, rows)
# Insert_Partia_leku(connection, rows)
# Insert_Zamowienia(connection, rows)
Insert_Informacje_o_zamowieniu(connection, rows)

