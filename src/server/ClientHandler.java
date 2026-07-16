package server;


import java.io.*;
import java.net.Socket;



public class ClientHandler implements Runnable {


    private Socket socket;

    private BufferedReader input;

    private PrintWriter output;

    private String username;



    public ClientHandler(Socket socket){


        this.socket = socket;


        try{


            input =
                    new BufferedReader(
                            new InputStreamReader(
                                    socket.getInputStream()
                            )
                    );


            output =
                    new PrintWriter(
                            socket.getOutputStream(),
                            true
                    );


        }
        catch(IOException e){


            e.printStackTrace();

        }

    }



    @Override
    public void run(){


        try{


            output.println(
                    "Enter username:"
            );


            username =
                    input.readLine();



            ChatServer.broadcast(
                    username
                    +" joined the chat",
                    this
            );



            String message;



            while(
                    (message=input.readLine())
                            != null
            ){


                if(message.equalsIgnoreCase("/quit")){

                    break;

                }



                else if(message.startsWith("@")){


                    output.println(
                            "Private message feature ready"
                    );


                }



                else{


                    ChatServer.broadcast(
                            username
                            +": "
                            +message,
                            this
                    );

                }


            }



        }
        catch(IOException e){


            System.out.println(
                    "Client disconnected"
            );

        }
        finally{


            try{

                socket.close();

            }
            catch(IOException e){}



            ChatServer.removeClient(this);

        }

    }



    public void sendMessage(String message){

        output.println(message);

    }



    public String getUsername(){

        return username;

    }


}