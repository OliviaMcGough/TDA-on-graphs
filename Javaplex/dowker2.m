function [sk0, sk1,sk2,sk3, sk4, sk5,sk6] = dowker2(A)

n=length(A);
diam=max(max(A));
% Build 0-skeleton
% Entry time of vertex i is just min(A(i,:))
eT=min(A,[],2);
sk0=[[1:n]',eT];

% Build 1-skeleton
q=nchoosek(1:n,2); %ideally use VChooseK(1:n,2); 
% Initialize sk1 with max entry time
sk1=[q,diam*ones(size(q,1),1)];
for ii=1:size(q,1)
    aI=A(q(ii,1),:);
    aJ=A(q(ii,2),:);
    aIJ=max([aI;aJ]);
    eT=min(aIJ);
    sk1(ii,end)=eT;
end
sk1(sk1(:,3)==1,:)=[];

if (nargout>2)
% Build 2-skeleton
q=nchoosek(1:n,3); %ideally use VChooseK(1:n,3); 
% Initialize sk2 with max entry time
sk2=[q,diam*ones(size(q,1),1)];
for ii=1:size(q,1)
    aI=A(q(ii,1),:);
    aJ=A(q(ii,2),:);
    aK=A(q(ii,3),:);
    aIJK=max([aI;aJ;aK]);
    eT=min(aIJK);
    sk2(ii,end)=eT;
end
sk2(sk2(:,4) ==1,:)=[];
end

if (nargout>3)
   % Build 3-skeleton
q=nchoosek(1:n,4); %VChooseK(1:n,4); 
% Initialize sk3 with max entry time
sk3=[q,diam*ones(size(q,1),1)];
for ii=1:size(q,1)
    aI=A(q(ii,1),:);
    aJ=A(q(ii,2),:);
    aK=A(q(ii,3),:);
    aL=A(q(ii,4),:);
    aIJKL=max([aI;aJ;aK;aL]);
    eT=min(aIJKL);
    sk3(ii,end)=eT;
end 
sk3(sk3(:,5) ==1,:)=[];
end

if (nargout>4)
q=nchoosek(1:n,5);
sk4=[q,diam*ones(size(q,1),1)];
for ii=1:size(q,1)
    aI=A(q(ii,1),:);
    aJ=A(q(ii,2),:);
    aK=A(q(ii,3),:);
    aL=A(q(ii,4),:);
    aM=A(q(ii,5),:);
    aIJKLM=max([aI;aJ;aK;aL;aM]);
    eT=min(aIJKLM);
    sk4(ii,end)=eT;
end
sk4(sk4(:,6) ==1,:)=[]
end

if (nargout>5)
q=nchoosek(1:n,6);
sk5=[q,diam*ones(size(q,1),1)];
for ii=1:size(q,1)
    aI=A(q(ii,1),:);
    aJ=A(q(ii,2),:);
    aK=A(q(ii,3),:);
    aL=A(q(ii,4),:);
    aM=A(q(ii,5),:);
    aN=A(q(ii,6),:);
    aIJKLMN=max([aI;aJ;aK;aL;aM;aN]);
    eT=min(aIJKLMN);
    sk5(ii,end)=eT;
end
sk5(sk5(:,7) ==1,:)=[]
end




if (nargout>6)
q=nchoosek(1:n,7);
sk6=[q,diam*ones(size(q,1),1)];
for ii=1:size(q,1)
    aI=A(q(ii,1),:);
    aJ=A(q(ii,2),:);
    aK=A(q(ii,3),:);
    aL=A(q(ii,4),:);
    aM=A(q(ii,5),:);
    aN=A(q(ii,6),:);
    aO=A(q(ii,7),:);
    aIJKLMNO=max([aI;aJ;aK;aL;aM;aN;aO]);
    eT=min(aIJKLMNO);
    sk6(ii,end)=eT;
end
sk6(sk6(:,8) ==1,:)=[]
end



end