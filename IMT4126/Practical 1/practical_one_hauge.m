%% General MATLAB Programming - Task 1
% Generate a random matrix A of dimension 10 × 10. Then modify the matrix A
% to obtainmatrix B by (a) replacing the 8th column elements to 0 (b) 
% assigning the 2nd row element to 1.

clear; % Clean the workspace
clc; % Clean the command window

A = rand(10,10);
B = A;
B(:,8) = 0;
B(2,:) = 1

%% Image Processing Using MATLAB - Task 2
% Assume that there are 2 images in the folder named images−db. Write a 
% Matlab program to read and display all images in the folder images − db.

clear; % Clean the workspace
clc; % Clean the command window

x = [];
images = dir('images-db/*.jpg'); % Reads the .jpg files in the "images-db" folder in the CURRENT directory
for i = 1:length(images)
    imagename = images(i).name;
    imagefolder = images(i).folder;
    imagepath = append(imagefolder, '/', imagename)
    image = imread(imagepath);    
    figure, imshow(image);
end

%% Image Processing Using MATLAB - Task 3
% Read the image I from the folder and show the result of Sobel and Canny 
% edge detectors.

clear; % Clean the workspace
clc;   % Clean the command window

imageI = 1; % Defining which image I to show. Can be incorporated in a loop.

imagelocation = dir('images-db/*.jpg'); % Reads the .jpg images stored in the folder in the CURRENT directory
imagename = imagelocation(imageI).name; 
imagefolder = imagelocation(imageI).folder; 
imagepath = append(imagefolder, '/', imagename); 
images = imread(imagepath);
grayimage = rgb2gray(images);

processedimage = edge(grayimage); % Sobel detection is standard in the edge function according to the documentation
displayedimage = figure, imshow(processedimage);
processedimage = edge(grayimage, 'canny');
displayedimage = figure, imshow(processedimage);