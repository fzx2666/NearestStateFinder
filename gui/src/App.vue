<template>
  <v-app id="inspire">
    <v-app-bar
      app
      color="white"
      flat
    >
      <v-container class="py-0 fill-height">
        <v-avatar
          class="mr-10"
          color="grey darken-1"
          size="32"
        ></v-avatar>

        <!--v-btn
          v-for="link in links"
          :key="link"
          text
        >
          {{ link }}
        </v-btn-->

        <v-spacer>
          
        </v-spacer>

        <v-responsive max-width="260">
          <v-text-field
            dense
            flat
            hide-details
            rounded
            solo-inverted
          ></v-text-field>
        </v-responsive>
      </v-container>
    </v-app-bar>

    <v-main class="grey lighten-3">
      <v-container>
        <v-row >
          <v-col cols="3">
            <v-card
              class="mx-auto rounded-lg"
              width="300"
            >
              <v-card-title>
                  Nearest Positions
              </v-card-title>
              <v-list three-line>
                <template v-for="(city, index) in cities">
                  <v-list-item
                    :key="index"
                  >
                    <v-list-item-avatar>
                      <v-icon>mdi-map-marker</v-icon>
                    </v-list-item-avatar>

                    <v-list-item-content>
                      <v-list-item-title v-html="city.name"></v-list-item-title>
                      <v-list-item-subtitle v-html="city.info"></v-list-item-subtitle>
                      <v-list-item-subtitle v-html="city.getDescription()"></v-list-item-subtitle>
                    </v-list-item-content>
                  </v-list-item>
                </template>
                <v-divider></v-divider>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title>
                      <span class="font-weight-thin">K nestest positions</span>
                    </v-list-item-title>
                    <v-list-item-subtitle>
                      <v-slider
                        v-model="numberOfCities"
                        step="1"
                        ticks="always"
                        tick-size="4"
                        max = "10"
                        min = "1"
                      ></v-slider>
                      
                      <v-btn
                        class="mx-2"
                        icon
                        small
                        @click="numberOfCities++"
                      >
                        <v-icon dark>
                          mdi-plus
                        </v-icon>
                      </v-btn>
                      {{numberOfCities}}
                      <v-btn
                        class="mx-2"
                        icon
                        small
                        @click="numberOfCities--"
                      >
                        <v-icon dark>
                          mdi-minus
                        </v-icon>
                      </v-btn>
                    </v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
              
            </v-card>
          </v-col>

          <v-col>
            <v-sheet
              min-height="70vh"
              rounded="lg"
              class="fill-height fill-height"
            >
            
            <GmapMap
              :center="{lat:40, lng:-95}"
              :zoom="4"
              map-type-id="terrain"
              class="fill-height fill-height"
              @click="this.onMapClick"
            >
              <GmapMarker
                :key="index"
                v-for="(m, index) in markers"
                :position="m.position"
                :clickable="true"
                :draggable="true"
                @click="center=m.position"
              />
              
              <GmapMarker
                :key="index+1"
                v-for="(city, index) in cities"
                :position="city.marker.position"
                :clickable="true"
                :draggable="true"
                @click="center=city.marker.position"
              />
            </GmapMap>
            </v-sheet>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
    <link href="https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/@mdi/font@4.x/css/materialdesignicons.min.css" rel="stylesheet">
    
  </v-app>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import HelloWorld from './components/HelloWorld.vue';
import {PythonShell} from 'python-shell'
import * as VueGoogleMaps from 'vue2-google-maps'

class Marker{
  public position = undefined
  constructor(latLng: any){
    this.position = latLng;
  }
}
class CityInfo{
  name = "cityname";
  info = "cityInfo";
  marker: Marker|undefined;
  dist = NaN;
  constructor(marker: Marker, name: string, info: string, dist: number){
    this.name = name;
    this.info = info;
    this.marker = marker;
    this.dist = dist;
  }
  public getlat(): number{
    const pos: any =  this.marker?.position;
    return pos?.lat();
  }  
  public getlng(): number{
    const pos: any =  this.marker?.position;
    return pos?.lng();
  }
  public getDescription(): string{
    return `Distance: ${this.dist}, Lat:${this.getlat()},Lng:${this.getlng()}`
  }
}
@Component({
  components: {
    HelloWorld,
  },
})


export default class App extends Vue {
  public numberOfCities = 1;
  public markers: Marker[] = [];
  public cities: CityInfo[] = [];
  pyPath = 'D:/repos/NearestStateFinder/';
  onMapClick(event: any): void{
    Vue.set(this.markers,0,new Marker(event.latLng));
    const lat = event.latLng.lat();
    const lng = event.latLng.lng();
    const shellOptions = {
      scriptPath: this.pyPath,
      pythonPath:'python3',
      pythonOptions: ['-u'],
      args: [lat,lng,this.numberOfCities,1,this.pyPath]
    }
    PythonShell.run('codeHandler.py',shellOptions,(err,result)=>{
      
      if(err==null&&result!=undefined){
        console.log(result[2]);
        const results = JSON.parse(result[2]);
        const cities: CityInfo[] = [];
        for(const res of results){

          const info = new CityInfo(new Marker(new (this.google().maps.LatLng)(res.lat,res.lon)),res.info,res.info,res.dist);
          cities.push(info);
          //console.log(new (this.google().maps.LatLng)(res.lat,res.lon))
        }
        this.cities = cities;
      }
      else{
        console.log(err);
        console.log(result);
      }
    });
  }
  public get google(){
    return VueGoogleMaps.gmapApi;
  }
}

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
