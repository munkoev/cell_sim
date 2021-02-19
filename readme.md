Дана доска размером M × N клеток.
Клетка может находиться в одном из двух состояний: 1 — живая, 0 — мёртвая.
Каждая клетка взаимодействует с восемью соседями.

Правила таковы:
- Живая клетка, у которой меньше двух живых соседей, погибает.
- Живая клетка, у которой два или три живых соседа, выживает.
- Живая клетка, у которой больше трёх живых соседей, погибает.
- Мёртвая клетка, у которой три живых соседа, возрождается.

Программа может:
— Случайным образом генерировать стартовое состояние или получать из списка;
— Каждую секунду выводить в консоль или в график новое состояние доски.