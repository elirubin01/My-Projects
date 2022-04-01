%This program takes an input in the form of a txt file called data.txt
%Each line contains x and y coordinates in the format "x y"
%Use Lagrange Polynomials to find the polynomial through the points

dataSize = [2 Inf];
file = fopen('data.txt', 'r');
data = fscanf(file, '%f %f', dataSize);
fclose(file);
data = data.';

matrixSize = size(data);
lagrange = strings(matrixSize(1));
finalPoly = "";
for i = 1: matrixSize(1)
    currX = data(i, 1);
    for n = 1: matrixSize(1)
        if n ~= i
            tempX = data(n, 1);
            newTerm = "(x - " + tempX + ") / (" + currX + " - "+ tempX + ") * ";
            lagrange(i) = append(lagrange(i), newTerm);
        end
    end
    if i == matrixSize(1)
        newTerm = "" + data(i, 2);
    else
        newTerm = data (i, 2) + " + ";
    end
    finalPoly = append(finalPoly, lagrange(i), newTerm);
end

minX = min(data(:,1));
maxX = max(data(:,1));
ezplot(finalPoly, [minX, maxX]);
hold on;
scatter(data(:, 1), data(:, 2));
grid on;
title("Polynomial");
xlabel("x");
ylabel("y");
hold off;