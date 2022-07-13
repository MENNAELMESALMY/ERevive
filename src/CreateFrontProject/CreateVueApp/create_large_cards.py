def generate_large_cards(cluster_name,endpoint,directory,
    is_single_entity=False,delete_route='',put_route='',post_route=''):

    table_headers_orig = list(endpoint['response'].keys())

    table_headers = [header.replace('.',' ').replace('_',' ')  for header in table_headers_orig]
    table_headers_orig = [header.replace('.','_').replace('_','_')  for header in table_headers_orig]

    # cluster_name = endpoint['cluster_name']
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
        if datatype=='bool':
            card_string += f'\t\t<input type="{datatype}" v-model="{param}" class="{datatype}">\n' 
        else:
            card_string += f'\t\t<input type="{datatype}" v-model="{param}" class="{datatype}" required>\n'
        if datatype == 'checkbox':
            card_string += '\t\t<label>Set Value</label>\n'
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
    card_string += '<h2>'+cluster_name+'</h2>'
    # if is_single_entity:
    #     card_string += f'''
    #     <div class="buttons">
    #         <router-link to="{post_route}" class="button">Add +</router-link>
    #         <router-link to="{put_route}" class="button">edit</router-link>
    #         <button class="button" @click='delete_entity'>delete</button>
	# 	</div>
    #     '''
    card_string +=    '''
    </div>
    '''
    card_string += '<h3>'+endpoint_name+'</h3>'
    card_string +='''
    <div>

    <div class='main_cards'>\n'''
    card_string += "\t\t<div v-for='(row,i) in card_data' :key='i'  class='big_card'>"
    for header in table_headers_orig:
        card_string += '\t\t\t<div class="attribute">'+header+' : {{row.' + header + '}}</div>\n'
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

<script>
    import { mapState } from "vuex";
    export default {
    name: "big_cards",
    props: {},
    data: function () {
    return {
'''
    for param,_,_,_ in query_params:
        card_string += '\t\t'+param.replace('.','_').replace(' ','_') + ':' + '"",\n'
    card_string += '''
    };
    },
    computed: {
    ...mapState({
    '''
    card_string += 'card_data: state => state.'\
                    +cluster_name+'.'+endpoint_name+',\n'
    card_string += '''}),},
    methods: {
    call_request() {
    '''
    card_string+= 'this.$store.dispatch("'+cluster_name +'/'+endpoint_name +'",\n\t\t {'
    for param,_,_,_ in query_params:
        card_string += "'"+param+"'" +': this.' + param.replace('.','_').replace(' ','_') + ',\n\t\t'

    card_string += '''
      });
    }
    }
    };
</script>
    '''
    f = open(directory, "w")
    f.write(card_string)
    f.close()