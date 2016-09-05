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
    deviceList->next;
  char *dispositivo = deviceList -> name;
  const struct ip_header *ip; /* Header del protocolo IP */
  pcap_t *captura; /* Instancia de pcap para realizar el sniffing */
  const u_char *paquete; /* El paquete obtenido */
  struct pcap_pkthdr h; /* Header del paquete (?) */
  
}


/* Por ahora, sniffing ilimitado */
int main(int argc, char *argv[])
{
  return(0);
}
