program Calculadora;

var
  num1, num2, resultado: real;
  operacao: char;

begin
  writeln('Calculadora em Pascal');
  write('Digite o primeiro número: ');
  readln(num1);
  write('Digite a operação (+, -, *, /): ');
  readln(operacao);
  write('Digite o segundo número: ');
  readln(num2);

  case operacao of
    '+': resultado := num1 + num2;
    '-': resultado := num1 - num2;
    '*': resultado := num1 * num2;
    '/': 
      if num2 <> 0 then
        resultado := num1 / num2
      else
      begin
        writeln('Erro: Divisão por zero não é permitida.');
        exit;
      end;
  else
    writeln('Operação inválida.');
    exit;
  end;

  writeln('Resultado: ', resultado:0:2);
end.
