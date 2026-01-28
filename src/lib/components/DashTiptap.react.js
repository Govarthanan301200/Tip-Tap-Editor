import React, { useEffect } from 'react';
import PropTypes from 'prop-types';
import { useEditor, EditorContent } from '@tiptap/react';
import StarterKit from '@tiptap/starter-kit';
import Mention from '@tiptap/extension-mention';
import suggestion from './suggestion';
import './DashTiptap.css';

const DashTiptap = (props) => {
    const { id, value, mentions, setProps } = props;

    const editor = useEditor({
        extensions: [
            StarterKit,
            Mention.configure({
                HTMLAttributes: {
                    class: 'mention',
                },
                suggestion: suggestion(mentions || []),
            }),
        ],
        content: value,
        onUpdate: ({ editor }) => {
            const html = editor.getHTML();
            if (setProps) {
                setProps({ value: html });
            }
        },
    });

    useEffect(() => {
        if (editor && value !== editor.getHTML()) {
            editor.commands.setContent(value);
        }
    }, [value, editor]);

    return (
        <div id={id}>
            <EditorContent editor={editor} />
        </div>
    );
};

DashTiptap.defaultProps = {
    mentions: [],
    value: '<p>Hello World! Type @ to mention someone.</p>'
};

DashTiptap.propTypes = {
    id: PropTypes.string,
    mentions: PropTypes.arrayOf(
        PropTypes.shape({
            id: PropTypes.oneOfType([PropTypes.string, PropTypes.number]).isRequired,
            label: PropTypes.string.isRequired,
        })
    ),
    value: PropTypes.string,
    setProps: PropTypes.func,
};

export default DashTiptap;