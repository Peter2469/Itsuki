import inspect
import io
import textwrap
import traceback
from collections import Counter
from contextlib import redirect_stdout
from random import randint

import discord
from discord.ext import commands

from secret import ownerid as oid


class evalCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        bot.stats = Counter()

    @commands.command(name='eval')
    async def _eval(self, ctx, *, body):

        if ctx.author.id == oid:
            """Evaluates python code"""
            env = {
                'ctx': ctx,
                'bot': self.bot,
                'channel': ctx.channel,
                'author': ctx.author,
                'guild': ctx.guild,
                'message': ctx.message,
                'source': inspect.getsource
            }

            def cleanup_code(content):
                """Automatically removes code blocks from the code."""
                # remove ```py\n```
                if content.startswith('```') and content.endswith('```'):
                    return '\n'.join(content.split('\n')[1:-1])

                # remove `foo`
                return content.strip('` \n')

            def get_syntax_error(e):
                if e.text is None:
                    return f'```py\n{e.__class__.__name__}: {e}\n```'
                return f'```py\n{e.text}{"^":>{e.offset}}\n{e.__class__.__name__}: {e}```'

            env.update(globals())

            body = cleanup_code(body)
            stdout = io.StringIO()
            err = out = None

            to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

            def paginate(text: str):
                '''Simple generator that paginates text.'''
                last = 0
                pages = []
                for curr in range(0, len(text)):
                    if curr % 1980 == 0:
                        pages.append(text[last:curr])
                        last = curr
                        appd_index = curr
                if appd_index != len(text) - 1:
                    pages.append(text[last:curr])
                return list(filter(lambda a: a != '', pages))

            try:
                exec(to_compile, env)
            except Exception as e:
                err = await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')
                return await ctx.message.add_reaction('\u2049')

            func = env['func']
            try:
                with redirect_stdout(stdout):
                    ret = await func()
            except Exception as e:
                value = stdout.getvalue()
                err = await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
            else:
                value = stdout.getvalue()
                if ret is None:
                    if value:
                        try:

                            await ctx.send(f'```py\n{value}\n```')
                        except:
                            paginated_text = paginate(value)
                            for page in paginated_text:
                                if page == paginated_text[-1]:
                                    out = await ctx.send(f'```py\n{page}\n```')
                                    break
                                await ctx.send(f'```py\n{page}\n```')
                else:
                    try:
                        out = await ctx.send(f'```py\n{value}{ret}\n```')
                    except:
                        paginated_text = paginate(f"{value}{ret}")
                        for page in paginated_text:
                            if page == paginated_text[-1]:
                                out = await ctx.send(f'```py\n{page}\n```')
                                break
                            await ctx.send(f'```py\n{page}\n```')

            if out:
                await ctx.message.add_reaction('\u2705')  # tick
            elif err:
                await ctx.message.add_reaction('\u2049')  # x
            else:
                await ctx.message.add_reaction('\u2705')
        else:
            embed = discord.Embed(title="No >:(", description="This is an owner command!",
                                  color=discord.Color(randint(0x0, 0xFFFFFF)))
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(evalCog(bot))
