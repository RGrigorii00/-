import T2;
import T3;
import T4;
import T5;

def T1():
	Heroes = [
		["Tank",   100],
		["Support", 20],
		["Ranger",  50],
	]

	#print(Heroes[0][1]);

	max_hp = 0;
	current_hp = 0;


	for i in range(len(Heroes)):
		#print(Heroes[i]);
		for i2 in range(len(Heroes[i])):
			#print(Heroes[i][i2]);
			current_hp = Heroes[i][i2 + 1];
			print(current_hp)
			if current_hp >= max_hp:
				max_hp = current_hp;
			break;
	print(max_hp);


T5.T5();























#human_import = int(input("Выберите героя (1 - 3): \n"));

##### 3 Задание #####
# Heroes --- HP       #--- Mana --- Damage

#Heroes = {
#	1 : 100, # Tank
#	2 :  20, # Support
#	3 :  50, # Ranger
#}

#print("Выбран герой номер: " + str(human_import) + "." + " Его очки здоровья: " + str(Heroes[human_import]));


##### 2 Задание #####
#max_hp = 0;
#current_hp = 0;

#for i in Heroes:
	#current_hp = Heroes[i];
	#if current_hp >= max_hp:
		#max_hp = current_hp;
		#break;
#print(Heroes[i]);

##### ------ #####
#for i in Heroes:
	#for i2 in Heroes[i]:
		#print(i , i2);
		#print(str())
		#current_hp = Heroes{i}{i2+1};
		#if current_hp >= max_hp:
		#	max_hp = current_hp;
		#break;
#print("Самый живучий герой имеет: " + str(max_hp) + " очков здоровья");