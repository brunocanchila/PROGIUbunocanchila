/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Vehiculo;

/**
 *
 * @author Bruno U
 */
public class VehiculoModerno {
     public static void main(String[] args) {
        
        
        
        
        vehiculo c = new vehiculo();
        
       c.setMarca("mercedes-benz");
       
       c.setModelo("AMG GT");
       
       c.setCaballosdefuerza("367 Caballos de fuerza");
       
       c.setTraccion("manual de 6 velocidades ");
       
       c.setKmph("245 KmpH aprox");
       
       
       System.out.println("Marca del vehiculo: "+  c.Marca);
       
         System.out.println("Modelo del vehiculo: "+ c.Modelo);
         
          System.out.println("Caballos de Fuerza: "+ c.caballosdefuerza);
          
           System.out.println("Traccion del vehiculo: "+c.traccion);
           
             System.out.println("Velocidad max Aprox. : "+ c.kmph);
        
    }
    
}
