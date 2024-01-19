h = T.val(find(strcmp(T.bas, "z")==0),find(strcmp(T.nonbas, "1")))

slack_tol = 1e-6

hneg = find(h<-slack_tol)

x0(hneg) = ones(length(hneg), 1)

T = addcol(T, x0, "x0", find(strcmp(T.nonbas, "1")));
## add artificial variable x0
z0 = zeros(1,length(T.nonbas));

z0(find(strcmp(T.nonbas,"x0")))=1;
## set z0 = 1 at column x0
T = addrow(T,z0,"z0",find(strcmp(T.bas,"z"))+1);
## add artificial variable z0
hid = zeros(length(T.bas),1)

for i = 1:length(hid)
if strcmp(T.bas{i}(1), "z") == 0
hid(i) = i
endif
endfor

h = T.val(find(hid>0), size(T.val,2))

r = find(h<=-1)



T.bas{s(1)}(2:end)

for k = 1:length(si)
si(k) = str2num(T.nonbas{k}(2:end))
endfor

T.nonbas(s)
