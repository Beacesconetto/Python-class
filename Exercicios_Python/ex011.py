larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('Sua parede tem a dimensão {}x{} e a sua área é de {}M²'. format(larg,alt,area))
print('Para pintar essa parede, você precisará de {}L de tinta' .format(area/2))