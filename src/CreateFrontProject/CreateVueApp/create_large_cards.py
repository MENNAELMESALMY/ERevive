def generate_large_cards(cluster_name,endpoint,directory,
    is_single_entity,delete_endpoint,put_endpoint,pks):

    table_headers_orig = list(endpoint['response'].keys())

    table_headers_orig = [header.replace('.','_').replace('_','_')  for header in table_headers_orig]

    endpoint_name = endpoint['endpoint_name']
    query_params = [(param,d,o,a) for param,d,o,a in endpoint['queryParams']]
    card_string = '''<template>
    <div class="dashboard">
        <div class="sidebar">'''
        
    if len(query_params)>0:
        card_string += '\t\t<p>Filters</p>\n'
    card_string += '\t\t<form>\n'
    card_string += '\t\t<div class="filters">\n'
    for param,datatype,operator,aggregate in query_params:
        param = param.replace('.','_')
        if operator == '<':operator = 'less than'
        elif operator == '>':operator = 'greater than'
        elif operator == '=' or operator == 'is':operator = 'equal to'
        elif operator == '!=':operator = 'not equal to'
        elif operator == '<=':operator = 'less than or equal to'
        elif operator == '>=':operator = 'greater than or equal to'
        elif operator == 'like':operator = 'regex matching (case invariant)'
        elif operator == 'not like':operator = 'regex matching (case invariant)'
        if not operator: operator = 'equal to'

        if datatype == 'str':datatype = 'text'
        elif datatype == 'int' or datatype == 'float':datatype = 'number'
        elif datatype=='bool':datatype = 'checkbox'
        elif datatype == 'date':datatype = 'date'
        else: datatype = 'text'
        card_string += '\t\t<div class="input_section">\n'
        card_string += '\t\t<div class="labels">\n'
        if aggregate: card_string += '\t\t<label> '+ aggregate+'</label><br>\n'
        card_string += '\t\t<label> '+ operator +'</label>\n'
        card_string += '\t\t<label>'+ param +'</label>\n'
        card_string += '\t\t</div>\n'

        card_string += '\t\t<div>\n'
        if operator == 'between':
            card_string += f'\t\t<input placeholder="from" type="{datatype}" v-model="{param}[0]" class="{datatype}" required>\n'
            card_string += f'\t\t<input placeholder="to" type="{datatype}" v-model="{param}[1]" class="{datatype}" required>\n'
        else:
            if datatype=='checkbox':
                card_string += f'\t\t<input type="{datatype}" v-model="{param}" class="{datatype}">\n' 
                card_string += '\t\t<label>Set Value</label>\n'
            else:
                card_string += f'\t\t<input type="{datatype}" v-model="{param}" class="{datatype}" required>\n'

        card_string += '\t\t</div>\n'
        card_string += '\t\t</div>\n'
        

    card_string += '\t\t</div>\n'  

    card_string +='''
        <input type="submit"
        value="Call endpoint"
        class="button"
        @click.prevent='call_request'>
        </form>
        </div>

<div class="content">
        <div class="table_nav">
        '''
    card_string += '<h2>'+cluster_name.replace("_cluster","").replace("_"," ")+'</h2>'
    card_string +=    '''
    </div>
    '''
    card_string += '<h3>'+endpoint_name+'</h3>'
    card_string +='''
    <div>

    <div class='main_cards'>\n'''

    card_string += "\t\t<div v-for='(row,i) in card_data' :key='i'  class='card_wrapper'>"

    card_string += "\t\t<div class='big_card'>"

    for header in table_headers_orig:
        card_string += '\t\t\t<div class="attribute"> <span style="fontWeight:bold;">'+header+' : </span>{{row.' + header + '}}</div>\n'
    
    card_string += '\t\t</div>'

    if(len(query_params)==0):
        card_string += '''
            <div class="card_header">
                <i  @click="route_edit(row)" class="fa fa-edit editIcon"></i>
                <i  @click="delete_obj(row)" class="fa fa-trash trashIcon" aria-hidden="true"></i>
            </div>\n'''
    card_string += '\t\t</div>'
    card_string += '''
        </div>


        </div>
        </div>
    </div>
</template>

<style lang="scss" scoped>
@import "../scss/dashboard.scss";
@import "../scss/big_card.scss";
</style>
'''

    card_string += '''
<script>
    import { mapState } from "vuex";
    export default {
    name: "dashBoard",
    props: {},
    data: function () {
    return {
'''
    for param,datatype,op,_ in query_params:
        if datatype == 'bool':
            card_string += '\t\t'+param.replace('.','_').replace(' ','_') + ':' + 'false,\n'
        elif op == 'between':
            card_string += '\t\t'+param.replace('.','_').replace(' ','_') + ':' + '["",""],\n'
        else:
            card_string += '\t\t'+param.replace('.','_').replace(' ','_') + ':' + '"",\n'
    card_string += '''
    };
    },
    computed: {
    ...mapState({
    '''
    card_string += 'card_data: state => state.'\
                    +cluster_name+'.'+endpoint_name+',\n'
    card_string += '''}),},'''
    if len(query_params)==0:
        card_string += '''
        async beforeMount(){
            await this.call_request();
        },
        '''
    card_string += '''
    methods: {
    async call_request() {
    '''
    card_string+= 'await this.$store.dispatch("'+cluster_name +'/'+endpoint_name +'",\n\t\t {'
    for param,_,_,_ in query_params:
        if op == 'in':
            card_string += "'"+param+"'" +': this.' + param.replace('.','_').replace(' ','_') + '.split(","),\n\t\t'
        else:
            card_string += "'"+param+"'" +': this.' + param.replace('.','_').replace(' ','_') + ',\n\t\t'
    card_string += '''
      });
    },
    async delete_obj(obj) {
    '''
    card_string+= 'await this.$store.dispatch("'+cluster_name +'/'+delete_endpoint +'",\n\t\t {'
    for pk,_ in pks:
        card_string += pk +': obj.' + pk + ',\n\t\t'
    card_string += '''
      });
      this.call_request();
    },
    route_edit(obj) {
    '''
    card_string+= 'let route = "'+ cluster_name +'_'+put_endpoint +'/"'
    for pk,_ in pks:
        card_string += '+obj.' + pk + '+"_"'
    
    card_string += f';\n\t\tthis.$store.commit("{cluster_name}/setCurObj", obj);'

    card_string += ''';
    this.$router.push({
      path: route,
    });
    }
    }
    };
</script>
    '''
    f = open(directory, "w")
    f.write(card_string)
    f.close()