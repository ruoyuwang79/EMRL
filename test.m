path='/Users/wangyihan';
img = imread(strcat(path,'/','1.jpg'));
img_g = rgb2gray(img);
[m,n] = size(img_g);
for i=1:m
    for j  = 1:n
        if img_g(i,j) >128
            img_g(i,j) = 255;
        else
            img_g(i,j) = 0;
        end
    end
end

img_small = imresize(img_g,[141,192]);
img_small2 = img_small;
[m,n] = size(img_small);
for i=1:m
    for j  = 1:n
        if img_small2(i,j) >170
            img_small2(i,j) = 255;
        else
            img_small2(i,j) = 0;
        end
    end
end
imshow(img_small2);