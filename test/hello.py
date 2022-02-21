#Recursion
print("1. Recursion\n")
def nilai_maksimal (list):
  nilai_terbesar = list[0]

  if len(list) > 1:
    next_nilai_terbesar = nilai_maksimal(list[1:])

    if next_nilai_terbesar > nilai_terbesar:
      nilai_terbesar = next_nilai_terbesar

  return nilai_terbesar

def nilai_minimal (list):
  nilai_terkecil = list[0]

  if len(list) > 1:
    next_nilai_terkecil = nilai_minimal(list[1:])

    if next_nilai_terkecil < nilai_terkecil:
      nilai_terkecil = next_nilai_terkecil
  
  return nilai_terkecil

a = [23, 12, -14, -20, 200, 159]
print(a)
print("Nilai terbesar:", nilai_maksimal(a))
print("Nilai terkecil:", nilai_minimal(a)) 
print("\n")

#List Comprehension
print("2. List Comprehension\n")
def faktorial(x):
	hasil = 1
	for i in range(1, x+1):
		hasil*=i
	return hasil

l_pertama = [2, 5, 7, 8, 10]	
l_hasil = [faktorial(i) for i in l_pertama]
print("Hasil faktorial dari list tersebut adalah : ", l_hasil)
print("\n")

#Closure
print("3. Closure\n")
def pangkat(n):
    def angka(x):
        return x**n
    return angka

li_angka = [1,2,3,4,5]
li_hasil_pangkat =list(map(pangkat(3), li_angka))
print(f"hasil dari list tersebut adalah : ", (li_hasil_pangkat))
print("\n")

#filter-lambda
print("4. Filter-lambda\n")
filter_list = list(filter(lambda angka: angka % 2 == 0 , li_hasil_pangkat))
print("(filter) bilangan genap :", filter_list)
print("\n")

#Currying
print("5. Currying\n")
def mengubah(b, c, d):
    def a(x):
        return b(c(d(x)))
    return a
      
def km_ke_m(dist): 
    return dist*1000
      
def m_ke_cm(dist): 
    return dist*100
      
def cm_ke_kaki(dist):
    return dist/30.48
      
if __name__ == '__main__':
    konversi = mengubah(km_ke_m, m_ke_cm, cm_ke_kaki)
    e = konversi(1000)
    print("Hasil dari konversi tersebut adalah",e)