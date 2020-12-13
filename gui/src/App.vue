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
                      <v-list-item-subtitle v-html="item.info"></v-list-item-subtitle>
                      <v-list-item-subtitle v-html="item.getDescription()"></v-list-item-subtitle>
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
import {gmapApi} from 'vue2-google-maps'

declare global {
    interface Window { child_process: any }
}
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
  onMapClick(event: any): void{
    Vue.set(this.markers,0,new Marker(event.latLng));
    const lat = event.latLng.lat();
    const lng = event.latLng.lng();
    const shellOptions = {
      scriptPath: 'D:/repos/NearestStateFinder/',
      pythonPath:'python3',
      pythonOptions: ['-u'],
      args: [lat,lng,this.numberOfCities,1]
    }
    console.log(shellOptions);
    PythonShell.run('codeHandler.py',shellOptions,(err,result)=>{
      console.log(err);
      console.log(result);
    });
  }
  public get google(): any{
    return gmapApi;
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
