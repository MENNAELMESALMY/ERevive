def generate_cards(endpoint,directory):
    with open(directory , 'w') as f:
        f.write('''
        <template>
        <div>
        </div>
        </template>

        <style lang="scss" scoped>
        </style>

        <script>
        export default {
    name:"createCards",
    }
        </script>
        ''')
