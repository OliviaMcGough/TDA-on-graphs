function[ints,l0,l1,l2,l3,l4,l5,l6]=computePers2(sk0,sk1,sk2,sk3,sk4,sk5,sk6,diam)

import edu.stanford.math.plex4.*;


if (nargin<5)
    stream=api.Plex4.createExplicitSimplexStream();
else
    stream = api.Plex4.createExplicitSimplexStream(diam); 
end

    if ~isempty(sk0)
        for v=1:size(sk0,1);
            stream.addVertex(sk0(v,1),sk0(v,2));
        end
    end

    if ~isempty(sk1)
        for e =1:size(sk1,1);
            stream.addElement(sk1(e,1:2), sk1(e,3)); 
        end
    end

    if ~isempty(sk2)
        for f=1:size(sk2,1);
            stream.addElement(sk2(f,1:3),sk2(f,4));
        end
    end

    if ~isempty(sk3)
        for g=1:size(sk3,1);
            stream.addElement(sk3(g,1:4),sk3(g,5));
        end
    end

    if ~isempty(sk4)
        for h=1:size(sk4,1);
            stream.addElement(sk4(h,1:5),sk4(h,6));
        end
    end
    
    if ~isempty(sk5)
        for i=1:size(sk5,1);
            stream.addElement(sk5(i,1:6),sk5(i,7));
        end
    end

    if ~isempty(sk6)
        for j=1:size(sk6,1);
            stream.addElement(sk6(j,1:7),sk6(j,8));
        end
    end 




stream.finalizeStream();

persistence = api.Plex4.getModularSimplicialAlgorithm(13,13);
% choosing 13 will allow for higher dim calcuations

intervals = persistence.computeIntervals(stream)
represent=persistence.computeAnnotatedIntervals(stream)

end