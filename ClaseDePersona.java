/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Personas;

/**
 *
 * @author Bruno U
 */
public class ClaseDePersona {
    
    String Nombre;
    String Apellidos;
    String Gmail;
    String Telefono;
    int Cedula;
    
    public ClaseDePersona(String Nombre,String Apellidos,int cedula,String Telefono,String Gmail){
    
    }
    
    public ClaseDePersona(){
        
    }

    public String getNombre() {
        return Nombre;
    }
    public void srtNombre(String Nombre){
        this.Nombre = Nombre;
    }
    
    public void setApellidos(String Apellidos){
        this.Apellidos = Apellidos;
    }

    public int getcedula(){
        return Cedula;
    }

    public void setCedula(int Cedula){
        this.Cedula = Cedula;
    }

    public String getGmail(){
        return Gmail;
    }

    public void setGmail(String Gmail){
        this.Gmail = Gmail;
    }

    public String getTelefono(){
        return Telefono;
    }

    public void setTelefono(String Telefono){
        this.Telefono = Telefono;
    }    
        
        
    
}
