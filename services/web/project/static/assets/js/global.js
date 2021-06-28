import * as heatMaps from './heatMaps.js'
import * as lineGraphs from './lineGraphs.js'

function build(){
    heatMaps.build()
    lineGraphs.build()
}

//var data = $('#my-data').data()
//console.log(data)
build()

window.addEventListener('resize', () => {
    build()
})