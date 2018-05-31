scatter(X,Y,'.')
Z=zscore(data);
D=pdist(Z);
Dsq=squareform(D);
%Here's the line where we generated a heatmap
HeatMap(Dsq);
L=linkage(D,'average');
id=cluster(L,'MaxClust',15);
scatter(X,Y,50,id,'.');
