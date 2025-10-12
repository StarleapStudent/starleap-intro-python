##### Recursion Example #####

# Run this file and inspect the output.  

def countdown(n, verbose = False):
    if verbose:
        print('countdown() called with argument: n = ', n)
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1, verbose)
    if verbose:
        print('Ending countdown() called with argument: n = ', n)

print("\nCountdown:")
countdown(5)

print("\nCountdown with details:")
countdown(2.5, verbose=True)


'''
call n=3
    call n=2
        call n=1
            call n=0
                blastoff
            end n=0
        end n=1
    end n=2
end n=3
'''