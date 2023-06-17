import os
import time
import shutil
import datetime


#обработка входных данных
print("Введите путь до родительского файла")
parent_path = input()

print('Введите имя файла')
file_name = input()

print('Введите путь до папки с бэкапами')
backup_path = input()

print('Введите интервал удаления файлов в минутах')
interval = int(input())
delta_interval = datetime.timedelta(minutes = interval)
time_interval = datetime.datetime.strptime(f'{str(delta_interval)}', '%H:%M:%S')

print('Введите интервал сохранения в секундах')
int_save=int(input())


file_type=''
try:
	file_name_str = file_name.split('.')
	file_pure_name = file_name_str[0]
	file_type = '.' + file_name_str[1]

except Exception as program:
	print('Используется файл без расширения')
	file_pure_name=file_name


files_name = []
files_date = []
files_time = []
while True:
	moment=datetime.datetime.now()      												#Определение текущей даты-времени
	moment_divided=str(moment).split(' ')												#Отделить текущую дату от времени
	time_divided=moment_divided[1].split('.')											#отсечение миллисекунд от времени
	moment_date=datetime.datetime.strptime(f'{str(moment_divided[0])}', '%Y-%m-%d')	 	#запись текущей даты
	moment_time=datetime.datetime.strptime(f"{str(time_divided[0])}",'%H:%M:%S')		#запись текущего времени
	time_record=str(moment_time).replace(':',' ')	
	time_for_record=time_record.split(' ')
	try:
		new_file_name=(f'{file_pure_name} {moment_date.date()} {time_for_record[1]}-{time_for_record[2]}-{time_for_record[3]}{file_type}').strip()
		file=shutil.copy(f"{parent_path}/{file_name}",f"{backup_path}/{new_file_name}")
		print(f"Сохранение файла {new_file_name}")
	except Exception as program:
		print('Файл недоступен в данный момент')
		time.sleep(int_save)
		continue

	#Заполнение импровизированной БД
	files_name.append(new_file_name)
	files_date.append(moment_date)
	files_time.append(moment_time)
	lenght=len(files_name)

	#Проверка по "БД"
	for i in range(lenght):
		if moment_date!=files_date[i-1]:
			files_date.pop(i-1)
			files_time.pop(i-1)
			try:
				os.remove(f"{backup_path}/{files_name[i-1]}")
				print(f"Удаление файла {files_name[i-1]}")
			except Exception as program:
				print('Файл уже не существует')
			files_name.pop(i-1)
		else:
			crutch=(moment_time-time_interval)
			#print(f'crutch:{crutch} : '+str(type(crutch)))
			crutch2=datetime.datetime.strptime(f"{str(crutch)}",'%H:%M:%S')
			if crutch2>files_time[i-1]:
				files_date.pop(i-1)
				files_time.pop(i-1)
				try:
					os.remove(f"{backup_path}/{files_name[i-1]}")
					print(f"Удаление файла {files_name[i-1]}")
				except Exception as program:
					print('Файл уже не существует')
				files_name.pop(i-1)


	time.sleep(int_save)


'''
print(f'moment_date:{moment_date} : '+str(type(moment_date)))
print(f'moment_time:{moment_time} : '+str(type(moment_time)))
print(f'timetime:{timetime} : '+str(type(timetime)))
print(f'file_pure_name:{file_pure_name}')
print(f'file_type:{file_type}')
print(f'delta_interval:{delta_interval} :' +str(type(delta_interval)))
print(f'time_interval:{time_interval} :' +str(type(time_interval)))
print(f'int_save:{int_save} : '+str(type(int_save)))
'''