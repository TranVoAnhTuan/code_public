function varargout = isUnboundedTableau(T, s, tol = 1e-6)
    H = T.val(1:size(T.val, 1) -1, 1:size(T.val, 2)-1);
    ## extract entries in pivot column
    h = T.val(1:size(T.val, 1) -1, 1:size(T.val, 2));
    ## extract last column
    neg = find(H(:,s)<= -tol);  
    ## extract negative entries in H(:, s)
    if(length(neg) >= 1)
        val = 0;
    else
        val = 1;
    endif
    varargout{1} = val;
    if nargout == 2
        varargout{2} = neg;
    endif


endfunction