% Clean up the workspace
clear;
clc;

logicTest = 1;
while logicTest == 1
    oldPassword = input('Enter old password: ', 's');
    clc;
   
    % (M) oldPassword has to be 8 characters
    if length(oldPassword) == 8
        
        while true
            newPassword = input('Enter new password: ', 's');
            clc;

            % Display the old and new password
            fprintf('Old Password: %s\nNew Password: %s\n\n', oldPassword, newPassword);

            % Policy counter
            policyCounter = 0;
            
            % Mandatory; flag
            mandatory = 0;
            
            % Contains a word; flag
            doesNotcontainAword = 1;

            disp('Policies Satisfied By The New Password:'); 

            % (M) newPassword has to be longer than or equal to oldPassword
            if length(newPassword) >= 8
                disp('* Longer than or equal to 8 characters');
                policyCounter = policyCounter + 1;
            else
                mandatory = mandatory + 1;
            end

            % (M) newPassword cannot be the same as, or contains parts of, 
            % the old password.
            if ~contains(newPassword, oldPassword)
                disp('* Not same as, or contains parts of, the old password.');
                policyCounter = policyCounter + 1;
            else
                mandatory = mandatory + 1;
            end

            % (+) newPassword has to contain at least one UPPER case letter
            if any(isstrprop(newPassword, 'upper'))
                disp('* Contains at least one upper character');
                policyCounter = policyCounter + 1;
            end

            % (+) newPassword has to contain at least one lower case letter
            if any(isstrprop(newPassword, 'lower'))
                disp('* Contains at least one lower character');
                policyCounter = policyCounter + 1;
            end

            % (+) newPassword has to contain at least one number
            if any(isstrprop(newPassword, 'digit'))
                disp('* Contains at least one number');
                policyCounter = policyCounter + 1;
            end    

            % (+) newPassword has to contain at least one special character
            if any(~isstrprop(newPassword, 'alphanum'))
                disp('* Contains at least one special character');
                policyCounter = policyCounter + 1;
            end

            % (+) newPassword is not a palindrome
            if any(newPassword ~= fliplr(newPassword))
                disp('* Is not a palindrome');
                policyCounter = policyCounter + 1;
            end  

            % (+) newPassword does not contain a dictionay word
            % Open dictionary file with 'read' permissions. Edit name 
            % and/or path to use another dictionary file
            fileID = fopen('MITdict.txt', 'r');
            MITdict = fgetl(fileID);
            
            % Only run if the file is not empty or until EOF
            while ischar(MITdict)
                % Get line form file
                MITdict = fgetl(fileID);
                % Skip lines with single charachters
                if length(MITdict) > 1
                    % Check if the new password contains a word in the
                    % dictionary
                    if contains(newPassword, MITdict, 'IgnoreCase', true)
                        % Stop the test on first occurrence of a word
                        doesNotcontainAword = 0;
                        break
                    end
                end
            end
            fclose(fileID);
            
            % If the 'Contains a word' value is not set, then add a point
            % to the policy counter and display the policy among the other
            % satisfied policies.
            if doesNotcontainAword == 1
                policyCounter = policyCounter + doesNotcontainAword;
                disp('* Does not contain a word');
            end

            % (+) newPassword does not conatin consecutive alphabets, 
            %upper or lower
            if ~any(regexp(lower(newPassword), '(.)\1'))
                disp('* Does not contain consecutive alphabets');
                policyCounter = policyCounter + 1;
            end

            % Calculate weakness score if the new password meats the 
            % policies and no mandatory requirement is missing
            if policyCounter ~= 0 && mandatory == 0
                weakScore = ((policyCounter*100)/9);
                fprintf('\nPassword Strength: %.2f%% \n\n', weakScore);

                % Check if weakness score is less than 50% 
                if weakScore < 50
                    % Try again
                    disp('Password is too weak to store. Try again');
                else
                % Check if weakness score is greater than 50% 
                    % Pass!
                    disp('Well Done! Good to Go');
                    break
                end
            else 
                fprintf('\nPassword does not meet the mandatory requirements. Try again in 5 seconds...\n\n');
                pause(5);
                clc;
            end
        end
        logicTest = 0;
    else
        disp('Old password has to be 8 charaters long.');
    end
end    