import periodictable

atomic_number = int(input("Atomic Number: "))
element = periodictable.elements[atomic_number]
print("Atomic Number: ",element.number)
print("Symbol: ",element.symbol)
print("Name: ",element.name)
print("Atomic Mass: ",element.mass)
print("Density: ",element.density)
print("Mass Unit: ",element.mass_units)
print("Absorption is:",element.neutron.absorption)



for el in periodictable.elements:
  print("%s %s %d"%(el.symbol,el.name, el.number))
  
  # Process all the isotopes for an element:
  for iso in el:
    print("%s %s"%(iso,iso.mass))

  print('_'*50)

