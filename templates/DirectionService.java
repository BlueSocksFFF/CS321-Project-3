
public interface TravelMode {
   void getEta();
   void getDirection();
}

public class Driving implements TravelMode {
    @Override
    public  Object getEta(){

    
        System.out.println("Calculating ETA (Driving)");
        return 1;
    }
    public getDirection(){
        System.out.println("Calculating Direction (Driving)");
        return 1;
    }

}

public class Bicycling implements TravelMode {
    @Override
    public  Object getEta(){
        System.out.println("Calculating ETA (Bicyling)");
        return 2;
    }
    public getDirection(){
        System.out.println("Calculating Direction (Bicycling)");
        return 1;
    }

}
public class Transit implements TravelMode {
    @Override
    public  Object getEta():
        System.out.println("Calculating ETA (Transit)"){
        return 3;
    }
    public getDirection(){
        System.out.println("Calculating Direction (Driving)");
        return 3;
    }

}

public class Walking implements TravelMode {
    @Override
    public  Object getEta(){
        System.out.println("Calculating ETA (Walking)");
        return 4;
    }
    public getDirection(){
        System.out.println("Calculating Direction (Driving)");
        return 4;
    }

}