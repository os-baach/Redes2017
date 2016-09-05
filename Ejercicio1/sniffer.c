#include <stdio.h>
#include <pcap.h>

/* Sniffing ilimitado (?) 
 * dev es el número del dispositivo sobre que el  sobre el que se hace 
 sniffing 
*/
int opcionIlimitada(int dev){
  pcap_if_t* deviceList; /* Lista de dispositivos de red */
  char errbuf[PCAP_ERRBUF_SIZE]; /* Buffer de errores */
  pcap_findalldevs(&deviceList, errbuf); /* Se llena la lista de 
					    dispositivos */
  int contador; /* Contador */
  for(contador = 0; contador < dev ; contador++)
    deviceList = deviceList->next;
  char *dispositivo = deviceList -> name;
  const struct ip_header *ip; /* Header del protocolo IP */
  pcap_t *captura; /* Instancia de pcap para realizar el sniffing */
  const u_char *paquete; /* El paquete obtenido */
  struct pcap_pkthdr h; /* Header del paquete (?) */

  printf("Capturaremos del dispositivo: %s \n", dispositivo);

  /*  captura = pcap_open_live(dispositivo, BUFSIZ, 1,1000, errbuf);

  if(captura == NULL){ /* Abrir el sniffer falló */
  /* printf("En captura ERROR: %s\n", errbuf);
    return EXIT_FAILURE;
  }*/
  return 0; 
}


/* Por ahora, sniffing ilimitado */
int main(int argc, char *argv[])
{
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

  //  opcion_ilimitada(disp);
  
  return(0);
}
