function f = fminfunc3(x)
i=1:7;
y(i) = 5 .*sin((x(i) - 0.5).^2).^2 + (x(i) - 1).^2 + exp(- x(i).^2);
f=sum(y);
end