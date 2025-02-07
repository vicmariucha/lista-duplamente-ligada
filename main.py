from Node import Node

class ListaDuplamenteLigada:
		def _init_(self):
				self.head = None  
				self.tail = None 

		def append(self, value):

				new_node = Node(value)
				if self.tail is None: 
						self.head = self.tail = new_node
				else:
						self.tail.next = new_node
						new_node.prev = self.tail
						self.tail = new_node

		def prepend(self, value):

				new_node = Node(value)
				if self.head is None:  
						self.head = self.tail = new_node
				else:
						new_node.next = self.head
						self.head.prev = new_node
						self.head = new_node

		def display(self):

				current = self.head
				while current:
						print(current.value, end=' <-> ' if current.next else '')
						current = current.next
				print()

		def remove(self, value):

				current = self.head
				while current:
						if current.value == value:
								if current.prev:
										current.prev.next = current.next
								else:
										self.head = current.next
								if current.next:
										current.next.prev = current.prev
								else:
										self.tail = current.prev
								return True  
						current = current.next
				return False  

		def _iter_(self):

				current = self.head
				while current:
						yield current
						current = current.next

def bubble_sort(arr, reverse=False):
		n = len(arr)
		for i in range(n):
				for j in range(0, n-i-1):
						if arr[j] > arr[j+1]:
								arr[j], arr[j+1] = arr[j+1], arr[j]
		if reverse:
				arr.reverse()
		return arr

def insertion_sort(arr, reverse=False):
		for i in range(1, len(arr)):
				key = arr[i]
				j = i - 1
				while j >= 0 and key < arr[j]:
						arr[j + 1] = arr[j]
						j -= 1
				arr[j + 1] = key
		if reverse:
				arr.reverse()
		return arr

def partition(arr, low, high):
		pivot = arr[high]
		i = low - 1
		for j in range(low, high):
				if arr[j] < pivot:
						i += 1
						arr[i], arr[j] = arr[j], arr[i]
		arr[i + 1], arr[high] = arr[high], arr[i + 1]
		return i + 1

def quick_sort(arr, low, high, reverse=False):
		if low < high:
				pi = partition(arr, low, high)
				quick_sort(arr, low, pi - 1)
				quick_sort(arr, pi + 1, high)
		if reverse:
				arr.reverse()
		return arr

def main():
		lista = ListaDuplamenteLigada()
		while True:
				try:
						num = int(input("Digite um número para adicionar à lista: "))
						lista.append(num)
						add_more = input("Deseja adicionar outro número? (sim/não): ").lower()
						if add_more != "sim" and add_more != "s":
								if lista.head is None or lista.head.next is None:
										print("Pelo menos dois números são necessários para ordenar.")
										continue
								else:
										break
				except ValueError:
						print("Por favor, insira um número inteiro válido.")

		if lista.head is None:
				print("Lista vazia. Programa encerrado.")
				return

		print("\nEscolha o algoritmo de ordenação:\n")
		print("1. Bubble Sort\n2. Insertion Sort\n3. Quick Sort\n")

		while True:
				try:
						choice = int(input("Digite sua escolha: "))
						if choice in [1, 2, 3]:
								break
						else:
								print("Escolha inválida. Por favor, selecione 1, 2 ou 3.")
				except ValueError:
						print("Por favor, insira um número correspondente à escolha.")

		while True:
				order = input("Deseja ordenar em ordem crescente ou decrescente? (C/D): ").upper()
				if order == "C":
						order = "crescente"
						break
				elif order == "D":
						order = "decrescente"
						break
				else:
						print("Opção inválida. Por favor, escolha entre C ou D.")

		numbers = [node.value for node in lista]  

		if choice == 1:
				sorted_numbers = bubble_sort(numbers, order == "decrescente")
		elif choice == 2:
				sorted_numbers = insertion_sort(numbers, order == "decrescente")
		else:
				sorted_numbers = quick_sort(numbers, 0, len(numbers) - 1, order == "decrescente")

		print("\nLista ordenada:", sorted_numbers)

if __name__ == "_main_":
		main()