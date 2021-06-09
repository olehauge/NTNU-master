% MAIN CODE
try 
    % Get user input for switch case
    n = input('Please enter your choice\n   1. Route Cipher\n   2. Vigenere Cipher\n   3. Four-square Cipher\n   4. Breaking Caesar Cipher using Frequency Analysis\n' );

    % Main part of code - switch case
    switch n
        case 1 % ROUTE CIPHER
            clc
            disp('Route Cipher')
            n = input('Please enter your choice\n   1. Encryption\n   2. Decrytpion\n');
            switch n
                case 1
                    clc
                    disp('Encryption')
                    routeCipherEncryption
                case 2
                    clc
                    disp('Decrytpion')
                    routeCipherDecryption
                otherwise
                    clc
                    disp('Not a valid value')
            end
        case 2 % VIGENÈRE CIPHER
            clc
            disp('Vigenere Cipher')
            n = input('Please enter your choice\n   1. Encryption\n');
            switch n
                case 1
                    clc
                    disp('Encryption')
                    vigenereCipherEncryption
                otherwise
                    clc
                    disp('Not a valid value')
            end    
        case 3 % FOUR-SQUARE CIPHER
            clc
            disp('Four-square Cipher')
            n = input('Please enter your choice\n   1. Encryption\n   2. Decrytpion\n');
            switch n
                case 1
                    clc
                    disp('Encryption')
                    fourSquareCipherEncryption
                case 2
                    clc
                    disp('Decrytpion')
                    fourSquareCipherDecryption
                otherwise
                    clc
                    disp('Not a valid value')
            end
        case 4 % FREQUENCY ANALYSIS
            clc
            disp('Breaking Caesar Cipher using Frequency Analysis')
            caesarCipherFrequencyAnalysis
        otherwise
            clc
            disp('Not a valid value')
    end
catch 
    % Catch the error of a user not entering a value, just hitting enter
    fprintf('\nUnvalid value entered!\nExiting application...\nGood bye!\n');
end    

% ROUTE CIPHER ENCRYPTION FUNCITON
function routeCipherEncryption
    ciphertext = [];
    % Get user input and make sure it is lower case
    plaintext = lower(input('Please enter plaintext: ', 's'));
    key = lower(input('Please enter route: ', 's'));
    
    grid = input('Please enter grid dimensions: ', 's');
    
    % Check the grid input is in the accepted format. Else inform the user.
    if contains(grid, '*')
        grid = split(grid, '*');
        row = str2num(cell2mat(grid(1)));
        column = str2num(cell2mat(grid(2)));
    else 
        disp('Please use a valid input (n*m) e.g. 3*9');
    end
    
    % Remove everything but letters
    remove = regexp(plaintext, '[^a-zA-Z]');
    plaintext(remove) = [];
    
    % Remove everything but letters and '-', since this is used in the
    % route keys
    remove = regexp(key, '[^a-zA-Z-]');
    key(remove) = [];
    
    % The possible keys for this route cipher
    secretKeyOption1 = 'horisontalroutefromtop-left';
    secretKeyOption2 = 'verticalroutefromtop-right';
    
    % Run the route cipher if the size of the matrix is greater than or 
    % equal to the length of the text. This way the user does not risk
    % unencrypted parts of his/hers text. 
    if row*column >= length(plaintext)
        
        % Check what key is being used and run that route cipher
        if strcmp(key, secretKeyOption1)
            
            matrix = repmat('0',row,column);
            
            % Insert the plaintext in the matrix
            i=1;
            for c = 1:column
                for r = 1:row
                    if i <= length(plaintext)
                        matrix(r,c)=plaintext(i);
                    else
                        matrix(r,c)='x';
                    end
                    i=i+1;
                end
            end
            
            % Read the letters form the matrix given by the route of
            % the key
            for r = 1:row
                
                % If it is an even row
                if rem(r,2)==0
                    ciphertext = [ciphertext, reverse(matrix(r,:))];
                else % If it is an odd row
                    ciphertext = [ciphertext, matrix(r,:)];
                end
            end
            
            % Finaly show the user the encyrpted message
            fprintf('Your enrypted text is: %s \n', upper(ciphertext));

        elseif strcmp(key, secretKeyOption2)
            
            matrix = repmat('0',row,column);
            
            % Insert the ciphertext in the matrix
            i=1;
            for c = 1:column
                for r = 1:row
                    if i <= length(plaintext)
                        matrix(r,c)=plaintext(i);
                    else
                        matrix(r,c)='x';
                    end
                    i=i+1;
                end
            end
            
            % Read the letters form the matrix given by the route of
            % the key
            i = rem(column,2);
            for c = 1:column
                
                % Go up and down starting from top right. Determine if the 
                % column is odd or even starting form the right most column
                if rem(column,2)==i
                    ciphertext = [ciphertext, reverse(matrix(:,c)')];
                else 
                    ciphertext = [ciphertext, matrix(:,c)'];
                end
            end
            
            % Finaly show the user the encyrpted message
            fprintf('Your enrypted text is: %s \n',upper(reverse(ciphertext)));
        else
            fprintf('Please use a valid key.\n');
        end
    else
        fprintf('Grid dimesions were too small.\n');
    end    
end

% ROUTE CIPHER DECRYPTION FUNCITON
function routeCipherDecryption
    plaintext = [];
    % Get user input and make sure it is lower case
    ciphertext = input('Please enter ciphertext: ', 's');
    key = lower(input('Please enter route: ', 's'));

    % Check the grid input is in the accepted format. Else inform the user.
    grid = input('Please enter grid dimensions: ', 's');
    if contains(grid, '*')
        grid = split(grid, '*');
        row = str2num(cell2mat(grid(1)));
        column = str2num(cell2mat(grid(2)));
    else 
        disp('Please use a valid input (n*m)');
    end
    
    % Remove everything but letters
    remove = regexp(ciphertext, '[^a-zA-Z]');
    ciphertext(remove) = [];
    
    % Remove everything but letters and '-', since this is used in the
    % route keys
    remove = regexp(key, '[^a-zA-Z-]');
    key(remove) = [];
   
    % The possible keys for this route cipher
    secretKeyOption1 = 'horisontalroutefromtop-left';
    secretKeyOption2 = 'verticalroutefromtop-right';
    
    % Run the route cipher if the size of the matrix is greater than or 
    % equal to the length of the text. This way the user does not risk
    % unencrypted parts of his/hers text. 
    if row*column >= length(plaintext)
    
        % Check what key is being used and run that route cipher
        if strcmp(key, secretKeyOption1)
            
            % Read the ciphertext into the matrix
            N = '%'+string(column)+'s';
            ciphertext = strread(ciphertext, N);
            matrixD = repmat('0',row,column);
            for r = 1:row
                % Check if row is even
                if rem(r,2)==0
                    matrixD(r,:) = reverse(char(ciphertext(r)));
                else 
                    matrixD(r,:) = char(ciphertext(r));
                end
            end
            
            % Read the plaintext form the matrix
            for c = 1:column
                plaintext = [plaintext, matrixD(:,c)'];
            end
            
            % Finaly show the user the decrypted message
            fprintf('Decrypted message: %s\n',plaintext);

        elseif strcmp(key, secretKeyOption2)
            
            % Read the ciphertext into the matrix
            matrixD = repmat('0',row,column);
            i=1;
            for c = 1:column
                for r = 1:row
                    if i <= length(ciphertext)
                        matrixD(r,c)=ciphertext(i);
                    else
                        matrixD(r,c)='x';
                    end
                    i=i+1;
                end
            end
            
            % Flip the matrix left to right
            matirxD = fliplr(matrixD);
            
            % Read the plaintext from the matrix
            for c = 1:column
                plaintext = [plaintext, reverse(matrixD(:,c)')];
            end

            % Finaly show the user the decrypted message
            fprintf('Your decrypted text is: %s\n', upper(reverse(plaintext)));
        else
            % Due to security reasons, do not tell the user that the route
            % is wrong. If someone is trying to crack the code this would
            % help them.
            fprintf('something went worng...\n');
        end
    else
         % Due to security reasons, do not tell the user that the size of
         % the matrix is wrong. If someone is trying to crack the code 
         % this would help them.
        fprintf('Something went wrong...\n');
    end
end

% VIGENÈRE CIPHER ENCRYPTION FUNCITON
function vigenereCipherEncryption
    % Create numbers for the alphabet
    alphabetEnd = 26;
    alphabet = 1:alphabetEnd;
    
    % Create the Tabula Recta by circularly shifting each row through the
    % entire matrix.
    tabulaRecta = [];
    for n = 0:25
        tabulaRecta = [tabulaRecta; circshift(alphabet, [0, -n])];
    end    
    
    % Get the input from the user and make it lower case
    plaintext = lower(input('Please enter plaintext: ', 's'));
    key = lower(input('Please enter secret key: ', 's'));
    
    % Remove everything but letters
    remove = regexp(plaintext, '[^a-zA-Z]');
    plaintext(remove) = [];

    % Remove everything but letters
    remove = regexp(key, '[^a-zA-Z]');
    key(remove) = [];
    
    % Convert the string values to numeric values matching the alphabet.
    plaintext = lower(plaintext) - double('a') + 1;
    key = key - double('a') + 1;

    % Run the cipher code if the key is equal to or shorter than the
    % plaintext
    if fix(numel(plaintext)/numel(key)) ~= 0
        
        % Repeat the key untill it is of equal length to the plaintext
        key = repmat(key, 1, fix(numel(plaintext)/numel(key)));
        key = [key, key(1:mod(numel(plaintext), numel(key)))];
        
        % Go through the matrix and find the values where n and m cross.
        % Save the result and show it to the user.
        ciphertext = arrayfun(@(m,n) tabulaRecta(m,n), key, plaintext)-1;
        ciphertext = upper(char(ciphertext + double('a')));
        
        fprintf('Your enrypted text is: %s \n', upper(ciphertext));

    else
        fprintf('The key is too long...\n')
    end
    
    
end

% FOUR-SQUARE CIPHER ENCRYPTION FUNCITON
function fourSquareCipherEncryption
    % Get input from the user and make i lower case
    plaintext = lower(input('Please enter plaintext: ','s')); 
    keys = lower(input('Please enter secret keys: ', 's'));
    
    % Split the key input and remove spaces
    keys = regexp(keys,',','split');
    key1 = keys{1}; 
    key2 = keys{2}; 
    key1 = key1(find(~isspace(key1)));
    key2 = key2(find(~isspace(key2)));

    % Remove repeated letters in keys in order to create ciphertext
    % matirces with correct amount of letters.
    key1 = unique(key1, 'stable');
    key2 = unique(key2, 'stable');
    
    alphabet = 'abcdefghiklmnopqrstuvwxyz';
    
    % Format the plaintext input
    plaintext = char(plaintext);
    remove = regexp(plaintext, '[^a-zA-Z]');
    plaintext(remove) = [];
    
    % Split message into digraphs
    diagraphedMessage = [];
    for len = 1: 2: length(plaintext)
        if len+1 < length(plaintext)
           diagraphedMessage = [diagraphedMessage, {plaintext(len:len+1)}];
        else
            % Add an x to make the length an even number
           diagraphedMessage = [diagraphedMessage, {[plaintext(len), 'x']}];
        end
    end
     
    % Create 3 matrices
    % Plaintext matrix
    plainTextMatrices = repmat('',5, 5);
    i=1;
    for column = 1:5
       for row = 1:5
           plainTextMatrices(column,row)= alphabet(i);
           i=i+1;
       end
    end
    
    % KEYWORD matrices
    topRightMatrix =  repmat('',5, 5);
    i=1;
    deletedLetter = 0;
    key1;
    for column = 1:5
       for row = 1:5
           if i <= length(key1)
               topRightMatrix(column,row)= key1(i);
               alphabet(alphabet==key1(i))='';
               deletedLetter = deletedLetter + 1;
           else
               % Input the rest of the alphabet after the keyword. Remove
               % the letters used in the keyword.
               topRightMatrix(column,row)= alphabet(i-deletedLetter);
           end
           i=i+1;
       end
    end
    topRightMatrix;
    
    % Re-fill the alphabet variable
    alphabet = 'abcdefghiklmnopqrstuvwxyz';

    bottomLeftMatrix =  repmat('',5, 5);
    i=1;
    deletedLetter = 0;
    key2;
    for column = 1:5
       for row = 1:5
           if i <= length(key2)
               bottomLeftMatrix(column,row)= key2(i);
               alphabet(alphabet==key2(i))='';
               deletedLetter = deletedLetter + 1;
           else
               % Input the rest of the alphabet after the keyword. Remove
               % the letters used in the keyword.
               bottomLeftMatrix(column,row)= alphabet(i-deletedLetter);
           end
           i=i+1;
       end
    end
    bottomLeftMatrix;

    %Encryption 
    ciphertext = [];
    for val = 1:length(diagraphedMessage)
       tmp = char(diagraphedMessage(val));
       [r1 c1] = find(plainTextMatrices==tmp(1));
       [r2 c2] = find(plainTextMatrices==tmp(2));
       ciphertext = [ciphertext, topRightMatrix(r1, c2)];
       ciphertext = [ciphertext, bottomLeftMatrix(r2, c1)];
    end  
    
    % Finaly show the encrypted message to the user
    fprintf('Your encypted text is: %s\n', upper(ciphertext));
end

% FOUR-SQUARE CIPHER DECRYPTION FUNCITON
function fourSquareCipherDecryption
    % Get user input
    ciphertext = lower(input('Please enter ciphertext: ', 's'));
    keys = lower(input('Please enter secret keys: ', 's'));
    
    % Format the ciphertext
    ciphertext = char(ciphertext);
    
    % Split the key input and remove spaces
    keys = regexp(keys,',','split');
    key1 = keys{1};
    key2 = keys{2}; 
    key1 = key1(find(~isspace(key1)));
    key2 = key2(find(~isspace(key2)));
    
    % Remove repeated letters in keys in order to create ciphertext
    % matirces with correct amount of letters.
    key1 = unique(key1, 'stable');
    key2 = unique(key2, 'stable');
    
    alphabet = 'abcdefghiklmnopqrstuvwxyz';
    
    % Split message into digraphs
    diagraphedCiphertext = [];
    for len = 1: 2: length(ciphertext)
       diagraphedCiphertext = [diagraphedCiphertext, {ciphertext(len:len+1)}];
    end
    
    % Plaintext matrices
    plainTextMatrices = repmat('',5, 5);
    i=1;
    for column = 1:5
       for row = 1:5
           plainTextMatrices(column,row)= alphabet(i);
           i=i+1;
       end
    end    
    
    % Key word matrices
    topRightMatrix =  repmat('',5, 5);
    i=1;
    deletedLetter = 0;
    key1;
    for column = 1:5
       for row = 1:5
           if i <= length(key1)
               topRightMatrix(column,row)= key1(i);
               alphabet(alphabet==key1(i))='';
               deletedLetter = deletedLetter + 1;
           else
               % Input the rest of the alphabet after the keyword. Remove
               % the letters used in the keyword.
               topRightMatrix(column,row)= alphabet(i-deletedLetter);
           end
           i=i+1;
       end
    end
    
    % Re-fill the alphabet variable
    alphabet = 'abcdefghiklmnopqrstuvwxyz';

    bottomLeftMatrix =  repmat('',5, 5);
    i=1;
    deletedLetter = 0;
    key2;
    for column = 1:5
       for row = 1:5
           if i <= length(key2)
               bottomLeftMatrix(column,row)= key2(i);
               alphabet(alphabet==key2(i))='';
               deletedLetter = deletedLetter + 1;
           else
               % Input the rest of the alphabet after the keyword. Remove
               % the letters used in the keyword.
               bottomLeftMatrix(column,row)= alphabet(i-deletedLetter);
           end
           i=i+1;
       end
    end
    
    % Decryption of ciphertext
    message=[];
    for val = 1:length(diagraphedCiphertext)
       tmp = char(diagraphedCiphertext(val));
        [r3 c3] = find(topRightMatrix==tmp(1));
        [r4 c4] = find(bottomLeftMatrix==tmp(2));
        message = [message, plainTextMatrices(r3, c4)];
        message = [message, plainTextMatrices(r4, c3)];
    end  
    
    %Finaly show the user the encypted message
    fprintf('Your decrypted text is: %s\n', upper(message));
end

% FREQUENCY ANALYSIS FUNCTION
function caesarCipherFrequencyAnalysis
    % Get user input and make it lower case
    ciphertext = lower(input('Please enter ciphertext to analyse: ', 's'));
    
    % Declaring variables 
    ciphertextLetterFreq = [];
    alphabet = 'a':'z';
    ciphertextGraphLabels = categorical({'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'});
    ciphertextGraphLabels = reordercats(ciphertextGraphLabels, {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'});
    englishGrapLabels = categorical({'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'});
    englishGrapLabels = reordercats(englishGrapLabels, {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'});
    enlgishLetterFreq = [8.12, 1.49, 2.71, 4.32, 12.02, 2.30, 2.03, 5.92, 7.31, 0.10, 0.69, 3.98, 2.61, 6.95, 7.68, 1.82, 0.11, 6.02, 6.28, 9.10, 2.88, 1.11, 2.09, 0.17, 2.11, 0.07];
       
    % Calculate the frequency of the letters in the ciphertext 
    for letter = 1:length(alphabet)
        numberOfLetters = count(ciphertext, alphabet(letter));
        % Frequency = occurence of letter / length of ciphertext
        numberOfLetters = (numberOfLetters / length(ciphertext)*100);
        ciphertextLetterFreq = [ciphertextLetterFreq, numberOfLetters];
    end

    % Suggest solution - by comparing the two biggest values in the
    % ciphertext and the english language
    [M1,I1] = max(ciphertextLetterFreq);
    [M2,I2] = max(enlgishLetterFreq);
    suggestedKey = mod(I1 - I2, 26);
    fprintf('The suggested key is: %s*. \n*The suggestion is more accurate for longer texts\n', string(suggestedKey));
    
    % Show 2 plots in one window
    tiledlayout(2,1)

    % Top Plot
    graph1 = nexttile;
    bar(ciphertextGraphLabels,ciphertextLetterFreq, 'r')
    title(graph1,'Letter Frequency in Inputed Text')
    
    % Bottom Plot
    graph2 = nexttile;
    bar(englishGrapLabels, enlgishLetterFreq)
    title(graph2,'English Letter Frequency')
    
   
    % Extra functionality - decryption function to test key found by 
    % analysing the data
    
    % Get user key suggestion
    caesarKey = input('Please enter secret key estimate: ');
    
    message = '';
    
    % Decryption
    for letter = 1:length(ciphertext)
        if contains(alphabet, ciphertext(letter))
            letterPosition = find(alphabet==ciphertext(letter));
            if mod((letterPosition - caesarKey), 26) ~= 0
                newLetterPos = mod((letterPosition - caesarKey), 26);
                newLetter = alphabet(newLetterPos);
            else 
                newLetter = alphabet(1);
            end    
            message = [message, newLetter];
        else
            message = [message, ciphertext(letter)];
        end
    end    
    
    % Finaly show the user the result of his guess
    fprintf('Your decrypted text is: \n\n%s\n', upper(message));
       
end