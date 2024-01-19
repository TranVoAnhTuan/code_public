function val = isFeasTableau(T, Ztol = 1e-6)
## usage: val = isFeasTableau(T)
## return 1 (true) if tableau is feasible, 0 (false) for otherwise

h = T.val(1:size(T.val,1)-1,size(T.val,2));

## get last column if tableau, ignore bottom row
neg = find(h <= -Ztol);
## find negative values in h
if length(neg) >= 1 ## at least on negative position
    val = 0;
else
    val = 1;
endif
endfunction