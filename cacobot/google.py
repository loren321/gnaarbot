import cacobot.base as base

@base.cacofunc
async def google(message, client, *args, **kwargs):
    '''
    **{0}google**
    Posts a google url to the query.
    *Example: `{0}google frog sucks`*
    '''

    query = message.content.split(" ")
    if (len(query) < 2):
        await client.send_message(message.channel, ':no_entry_sign: {}: You must provide a search query'.format(message.author.mention))
        return
    query.pop(0)
    query = "+".join(query)
    search_url = "http://google.com/search?q=" + query
    await client.send_message(message.channel, search_url)
