function s = pivotColumn(T, Ztol = 1e-6)
## usage s = pivotColumn(T, Ztol)
##
c = T.val(size(T.val,1), 1:size(T.val, 2)-1);
s = find(c <= Ztol);
endfunction