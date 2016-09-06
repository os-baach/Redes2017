#include <stdio.h>
#include <stdlib.h>
#include <pcap.h>
#include <arpa/inet.h>
#include "sniffer.h"

/* Declaración de funciones */
/* Sniffing ilimitado */
int opcion_ilimitada(int dispositivo);
/* Imprime un paquete */
void imprime_paquete(u_char *args, const struct pcap_pkthdr *header, const u_char *packet);

/* Por ahora, sniffing ilimitado */
int main(int argc, char *argv[]){
  /* Se imprime la lista de dispositivos */
  pcap_if_t* deviceList; /* Lista de dispositivos de red */
  char errbuf[PCAP_ERRBUF_SIZE]; /* Buffer de errores */
  pcap_findalldevs(&deviceList, errbuf); /* Se llena la lista de 
					    dispositivos */
  int contador = 1; /* Contador */
  while(deviceList->next != NULL){
    printf("Dipositivo %d: %s\n", contador, (deviceList->name));
    deviceList = deviceList->next;
    ++contador;
  }
  int disp; /* Número del dispositivo a analizar */

  printf("Escriba el nombre del dispositivo a analizar: \n");
  scanf("%d", &disp);

  opcion_ilimitada(disp);
  
  return(0);
}

void imprime_paquete(u_char *args, const struct pcap_pkthdr *header,
		     const u_char *paquete){
  char errbuf[PCAP_ERRBUF_SIZE]; /* Buffer de errores */
  const struct ip_header *ip;
  
  if(paquete == NULL){
     printf("Al recibir un paquete ERROR: %s \n",errbuf);
     return;
   }
   printf("Imprimimos el paquete\n");
   int i;
   for(i = 0; i < header->len; i++){
     printf("%x ", paquete[i]);
   }
   printf("\n");
  
   ip = (struct ip_header*)(paquete + TAM_ETHERNET);
   printf("(%x )%s -> (%x)%s \n",ip -> ip_src, inet_ntoa(ip->ip_src),((*ip).ip_dst),inet_ntoa(ip->ip_dst));
   printf("Protocolo :%x\n", ip->ip_p);
  
}


/* Sniffing ilimitado (?) 
 * dev es el número del dispositivo sobre que el  sobre el que se hace 
 * sniffing (se le resta 1 para facilidad del usuario) */
int opcion_ilimitada(int dev){
  dev--; /* Este paso se hace para no mostrarle al usuario dispositivos entre 
	  * 0 y n-1 */
  pcap_if_t* deviceList; /* Lista de dispositivos de red */
  char errbuf[PCAP_ERRBUF_SIZE]; /* Buffer de errores */
  pcap_findalldevs(&deviceList, errbuf); /* Se llena la lista de 
					  * dispositivos */
  int contador; /* Contador */
  for(contador = 0; contador < dev ; contador++)
    deviceList = deviceList->next;
  char *dispositivo = deviceList -> name;
  const struct ip_header *ip; /* Header del protocolo IP */
  pcap_t *captura; /* Instancia de pcap para realizar el sniffing */
  const u_char *paquete; /* El paquete obtenido */
  struct pcap_pkthdr h; /* Header del paquete (?) */
  char *filtro = "port 80"; /* Para sólo capturar http */
  struct bpf_program fp; /* Aquí almacenaremos el filtro compilado */
  bpf_u_int32 mask; /* Máscara de red */
  bpf_u_int32 net; /* Dirección ip */
  
  printf("Capturaremos del dispositivo: %s \n", dispositivo);

  captura = pcap_open_live(dispositivo, BUFSIZ, 1, 100, errbuf); 
  
  if(captura == NULL){ /* Abrir el sniffer falló */
    printf("En captura ERROR: %s\n", errbuf);
    return EXIT_FAILURE;
  }
  
  /* Sacamos ip y máscara del dispositivo */
  if (pcap_lookupnet(dispositivo, &net, &mask, errbuf) == -1) {
    /* Falló */
    fprintf(stderr, "No se pudo obtener la máscara de %s: %s\n",
	    dispositivo, errbuf);
    net = 0;
    mask = 0; 
  }

  /* Compilamos el filtro para que sea reconocido por pcap */
  if (pcap_compile(captura, &fp, filtro, 0, net) == -1) {
    fprintf(stderr, "No se pudo compilar el filtro %s: %s\n",
	    filtro, pcap_geterr(captura));
    exit(EXIT_FAILURE);
  }

  /* Se aplica el filtro compilado */
  if (pcap_setfilter(captura, &fp) == -1) {
    /* Falló */
    fprintf(stderr, "No se pudo instalar el filtro %s: %s\n",
	    filtro, pcap_geterr(captura));
    exit(EXIT_FAILURE);
  }

  /* Se hace sniffing indefinidamente. 
   * La función auxiliar imprime_paquete nos ayuda a imprimir los paquetes 
   * obtenidos  */
  pcap_loop(captura, -1, imprime_paquete, NULL);
 
  /* Limpieza */
  pcap_freecode(&fp);
  pcap_close(captura);
  printf("\nCaptura completa.\n");
  return EXIT_SUCCESS;  
}
