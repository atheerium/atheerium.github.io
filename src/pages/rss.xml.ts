import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';

export async function GET(context) {
  const articles = await getCollection('articles', ({ data }) => !data.draft);
  const research = await getCollection('research', ({ data }) => !data.draft);
  const notes = await getCollection('notes', ({ data }) => !data.draft);

  const allPosts = [...articles, ...research, ...notes].sort(
    (a, b) => b.data.pubDate.getTime() - a.data.pubDate.getTime()
  );

  return rss({
    title: 'Atheerium',
    description: 'Domain investing, freelancing, and building in public.',
    site: context.site,
    items: allPosts.map((post) => {
      const collection = post.collection;
      return {
        title: post.data.title,
        pubDate: post.data.pubDate,
        description: post.data.description,
        link: `/${collection}/${post.id.replace('.md', '')}/`,
      };
    }),
    customData: '<language>en-us</language>',
  });
}
