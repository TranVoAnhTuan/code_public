function t = isFeasDualTableau(T, Ztol = 1e-5)
cnr = find(strcmp(T.bas,"z"));
cnc = find(strcmp(T.nonbas,"1")==0);
c = T.val(cnr,cnc);
cneg = find(c < -Ztol);
if length(cneg) >= 1
    t = 0;
else
    t = 1
end