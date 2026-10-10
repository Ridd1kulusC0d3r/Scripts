def add(a, b)
  return a + b
end

def subtract(a, b)
  return a - b
end

def multiply(a, b)
  return a * b
end

def divide(a, b)
  return a / b
end

puts "Calculadora Simples"
puts "Escolha a operação:"
puts "1. Adição"
puts "2. Subtração"
puts "3. Multiplicação"
puts "4. Divisão"

choice = gets.chomp.to_i

puts "Digite o primeiro número:"
num1 = gets.chomp.to_f

puts "Digite o segundo número:"
num2 = gets.chomp.to_f

case choice
when 1
  result = add(num1, num2)
  operator = "+"
when 2
  result = subtract(num1, num2)
  operator = "-"
when 3
  result = multiply(num1, num2)
  operator = "*"
when 4
  result = divide(num1, num2)
  operator = "/"
else
  puts "Opção inválida."
  exit
end

puts "#{num1} #{operator} #{num2} = #{result}"
