function r = pivotRow(T, s, tol = 1e-8)
## usage = r = pivotRow(T,s,tol)
## find candidate for pivot row
hid = zeros(length(T.bas),1)

for i = 1:length(hid)
if strcmp(T.bas{i}(1), "z") == 0
hid(i) = i
endif
endfor
cnc = find(strcmp(T.nonbas,"1")==0);
    ## extract entries in pivot column
h = T.val(find(hid>0),size(T.val,2));
    ## extract last column
    H = T.val(find(hid>0),cnc);

    neg = find(H(:,s)<= -tol);
    ## extract negative entries in H(:, s)
    hneg = h(neg);
    Hneg = H(neg,s);
    ratio = -hneg./Hneg;
    ## ratio h(i)/H(i,s) for H(i,s)<0
    r = find(ratio == min(ratio));
    ## find index of min in ratio vector
    r = neg(r);
    ## extract exact row index
endfunction