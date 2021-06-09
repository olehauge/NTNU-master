function data=LoadData(n)
% Read data from file
    data=readtable(strcat(num2str(n),'.txt'),'Delimiter','|');
end