/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Personas;

/**
 *
 * @author Bruno U
 */
public class Persona1 {
     public static void main(String[] args) {

        clasepersona p = new clasepersona();
        
        p.setNombre("bruno david");
        p.setApellidos("canchila bahamon");
        p.setCedula("1128049779");
        p.setCorreo("brunocanchila240@gmail.com");
        p.setTelefono("3316731470");
    
        
        System.out.println("\n Mi nombre es: "+ p.Nombre);
        System.out.println("Mis apellidos: "+ p.Apellidos);
        System.out.println("Mi cedula es: "+ p.Cedula);
        System.out.println("Mi correo es: "+ p.Correo);
        System.out.println("Mi telefono es: "+ p.Telefono);
        
    }
    
}
}
