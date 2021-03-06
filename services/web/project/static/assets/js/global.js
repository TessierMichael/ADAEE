import * as heatMaps from './heatMapsCases.js'
import * as lineGraphs from './lineGraphsCases.js'
import * as metric from './aggregatedMetric.js'

function build(){
    heatMaps.build()
    lineGraphs.build(null)
    metric.build()
}

//var data = document.querySelector('#mydata')
//var cases = eval('(' + data.dataset.cases + ')')
//console.log(cases)
build()

window.addEventListener('resize', () => {
    build()
})