package server;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;


public class ChatServer {


    private static final int PORT = 5000;


    static ArrayList<ClientHandler> clients =
            new ArrayList<>();


    public static void main(String[] args) {


        System.out.println(
                "===================================="
        );

        System.out.println(
                " Java Chat Server Started"
        );

        System.out.println(
                " Listening on port: "
                + PORT
        );

        System.out.println(
                "===================================="
        );


        try(ServerSocket serverSocket =
                    new ServerSocket(PORT)) {


            while(true) {


                Socket socket =
                        serverSocket.accept();


                ClientHandler client =
                        new ClientHandler(
                                socket
                        );


                clients.add(client);


                Thread thread =
                        new Thread(client);


                thread.start();

            }


        }
        catch(IOException e) {


            System.out.println(
                    "Server Error: "
                    + e.getMessage()
            );
        }

    }



    public static void broadcast(
            String message,
            ClientHandler sender
    ){


        for(ClientHandler client : clients){


            if(client != sender){

                client.sendMessage(message);

            }

        }


        ChatLogger.log(message);

    }



    public static void removeClient(
            ClientHandler client
    ){

        clients.remove(client);


        String msg =
                client.getUsername()
                +" left the chat";


        broadcast(msg, client);

    }


}